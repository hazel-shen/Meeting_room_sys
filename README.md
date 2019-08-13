# COSCUP Demo - Meeting Room System

Reference engineering blog link: 

This is the sample code of for Meeting Room demo.
It was modified by LINE example code: https://github.com/line/line-things-starter
And Sparkfun GridEye example code: https://github.com/sparkfun/SparkFun_GridEYE_Arduino_Library

## Prepare

1. Raspberry pi 3B+ *1
2. ESP32 *1
3. SparkFun Grid-EYE Infrared Array Breakout - AMG8833 (Qwiic) (SEN-14607)*
</br>(Or whatelse you like)


## Setup

1. Import code from ESP32 with COSCUP_ESP32_DEMO/COSCUP_ESP32_DEMO.ino and replace the ${SERVICE_UUID}
2. Run COSCUP_RASPI_Thermal/thermal_cam.py on your raspberry pi 3B+
3. Deployed LIFF web app here and <a style="color: red;" href="https://github.com/hazel-shen/2019_coscup_chatbot"> CHAT BOT</a>
4. Turn on your LINE APP, scan this QRCode to enable LINE Things
<br>![](https://developers.line.biz/media/line-things/qr_code-311f3503.png)<br>
5. And then you can see your device on LINE Things list
<br><img style="width:200px;" src="https://i.imgur.com/PPItSDD.png"><br>


## Reference

For details on Bluetooth LE plugin API for LINE Things on LIFF, please refer to the following document (English to follow shortly):

https://developers.line.biz/ja/reference/line-things/
