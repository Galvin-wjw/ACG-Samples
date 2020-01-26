package com.baidu.galvin;

import com.baidubce.auth.DefaultBceCredentials;
import com.baidubce.auth.SignOptions;
import com.baidubce.http.HttpMethodName;
import com.baidubce.internal.InternalRequest;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import okhttp3.*;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.*;

import static org.apache.http.HttpHeaders.AUTHORIZATION;

public class SetCdnOrigin {
    public static void main(String[] args) throws URISyntaxException {
        GetAkSk getAkSk = new GetAkSk();
        String keyArray[] = getAkSk.toArrayByFileReader1("key.txt");
        String ACCESS_KEY = keyArray[0];                   // 用户的Access Key ID
        String SECRET_KEY = keyArray[1];           // 用户的Secret Access Key


        BceV1Signer bceV1Signer = new BceV1Signer();
        URI uri = new URI("http", "cdn.baidubce.com", "/v2/domain/test-sig.e-galvin.cn/config", "origin",null);
        InternalRequest request = new InternalRequest(HttpMethodName.PUT, uri);

        Map<String, String> headerMap = new HashMap<String, String>();
        headerMap.put("host", "cdn.baidubce.com");

        Map<String,String> params = new HashMap();
        params.put("origin", null);

        Set<String> headersToSignSet = new HashSet<String>();
        headersToSignSet.add("host");
        SignOptions signOptions = new SignOptions();
        signOptions.setHeadersToSign(headersToSignSet);
        request.setSignOptions(signOptions);
        request.setParameters(params);



        DefaultBceCredentials defaultBceCredentials = new DefaultBceCredentials(ACCESS_KEY, SECRET_KEY);

        bceV1Signer.sign(request, defaultBceCredentials);

        System.out.println(request.getHeaders().get(AUTHORIZATION));



        OkHttpClient okHttpClient = new OkHttpClient();

        Map<String,String> peer = new HashMap();
        peer.put("peer","http://galvin-beijing.bj.bcebos.com:8888");

        List<Map> person=new ArrayList<>();
        person.add(peer);

        Map<String,List> map=new HashMap<String,List>();
        map.put("origin",person);



        ObjectMapper M = new ObjectMapper();

        String json="";
        try {
            json = M.writeValueAsString(map);
        } catch (JsonProcessingException e) {
            System.out.println(e.getLocalizedMessage());
        }


        MediaType JSON = MediaType.parse("application/json; charset=utf-8");
        RequestBody requestBody = RequestBody.create(JSON,json);


        final Request httpRequest = new Request.Builder()
                .url(uri.toString())
                .addHeader(AUTHORIZATION, request.getHeaders().get("Authorization"))
                .put(requestBody)//默认就是GET请求，可以不写
                .build();
        Call call = okHttpClient.newCall(httpRequest);
        try {
            Response response = call.execute();
            System.out.println(response.code());
            if (response.body()!=null) {
                System.out.println(response.body().string());
            }
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}
