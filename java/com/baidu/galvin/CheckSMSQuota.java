package com.baidu.galvin;

import com.baidubce.auth.DefaultBceCredentials;
import com.baidubce.auth.SignOptions;
import com.baidubce.http.HttpMethodName;
import com.baidubce.internal.InternalRequest;
import okhttp3.*;

import java.io.*;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.*;

import static org.apache.http.HttpHeaders.AUTHORIZATION;

public class CheckSMSQuota {


    public static void main(String[] args) throws URISyntaxException {

        GetAkSk getAkSk = new GetAkSk();
        String keyArray[] = getAkSk.toArrayByFileReader1("key.txt");
        String ACCESS_KEY = keyArray[0];                   // 用户的Access Key ID
        String SECRET_KEY = keyArray[1];           // 用户的Secret Access Key


        BceV1Signer bceV1Signer = new BceV1Signer();
        URI uri = new URI("http", "sms.bj.baidubce.com", "/v1/quota", null);
        InternalRequest request = new InternalRequest(HttpMethodName.GET, uri);

        Map<String, String> headerMap = new HashMap<String, String>();
        headerMap.put("host", "sms.bj.baidubce.com");

        Set<String> headersToSignSet = new HashSet<String>();
        headersToSignSet.add("host");
        SignOptions signOptions = new SignOptions();
        signOptions.setHeadersToSign(headersToSignSet);
        request.setSignOptions(signOptions);

        DefaultBceCredentials defaultBceCredentials = new DefaultBceCredentials(ACCESS_KEY, SECRET_KEY);

        bceV1Signer.sign(request, defaultBceCredentials);

        System.out.println(request.getHeaders().get(AUTHORIZATION));


        OkHttpClient okHttpClient = new OkHttpClient();
        final Request httpRequest = new Request.Builder()
                    .url(uri.toString())
                    .addHeader(AUTHORIZATION, request.getHeaders().get("Authorization"))
                    .get()//默认就是GET请求，可以不写
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
