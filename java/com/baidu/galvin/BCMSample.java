package com.baidu.galvin;

import com.baidubce.auth.DefaultBceCredentials;
import com.baidubce.auth.SignOptions;
import com.baidubce.http.HttpMethodName;
import com.baidubce.internal.InternalRequest;
import okhttp3.Call;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

import static org.apache.http.HttpHeaders.AUTHORIZATION;

public class BCMSample {
    public static void main(String[] args) throws URISyntaxException {
        GetAkSk getAkSk = new GetAkSk();
        String keyArray[] = getAkSk.toArrayByFileReader1("key.txt");
        String ACCESS_KEY = keyArray[0];                   // 用户的Access Key ID
        String SECRET_KEY = keyArray[1];           // 用户的Secret Access Key


        BceV1Signer bceV1Signer = new BceV1Signer();
        URI uri = new URI("http", "bcm.bj.baidubce.com", "/json-api/v1/metricdata/f2205b52fe1a46d5bb69b271bf88603d/BCE_BOS/BucketSpaceUsedBytes",
                "dimensions=BucketId:galvin&endTime=2019-05-31T13:10:01Z&periodInSecond=600&startTime=2019-05-30T13:00:01Z&statistics[]=sum,average,sampleCount",null);
        InternalRequest request = new InternalRequest(HttpMethodName.GET, uri);

        Map<String, String> headerMap = new HashMap<>();
        headerMap.put("host", "bcm.bj.baidubce.com");

        Map<String,String> params = new HashMap<>();
        params.put("dimensions","BucketId:galvin");
        params.put("endTime","2019-05-31T13:10:01Z");
        params.put("periodInSecond","600");
        params.put("startTime","2019-05-30T13:00:01Z");
        params.put("statistics[]","sum,average,sampleCount");


        Set<String> headersToSignSet = new HashSet<>();
        headersToSignSet.add("host");

        SignOptions signOptions = new SignOptions();
        signOptions.setHeadersToSign(headersToSignSet);

        request.setSignOptions(signOptions);
        request.setParameters(params);

        DefaultBceCredentials defaultBceCredentials = new DefaultBceCredentials(ACCESS_KEY, SECRET_KEY);

        bceV1Signer.sign(request, defaultBceCredentials);

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
