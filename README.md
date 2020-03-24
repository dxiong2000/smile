# smile
Currently, if you want to sign into your Windows laptop or desktop computer using your webcam [(Windows Hello)](https://www.microsoft.com/en-us/windows/windows-hello), you would have to use [a special (and expensive) webcam](https://www.logitech.com/en-us/product/brio) with built in IR sensors for biometric scanning. Although [some laptops](https://www.microsoft.com/en-us/surface) come built in with these IR cameras, an overwhelming portion of the laptop market does not have a Windows Hello compatible webcam. 

I decided to work on this project because I, like many others, want to enjoy the hassle-free login experience that Windows Hello offers without shelling out hundreds of dollars for a new webcam or a Surface Pro. 

I tackle this problem by taking multiple frame stills from the webcam when the user is on the login screen, and comparing those images to a reference image. The comparison is done using the [face_recognition](https://github.com/ageitgey/face_recognition) Python module. I know this method of facial recognition isn't as accurate or as secure as the IR sensor alternative, but with an accuracy of 99.38%, I think that it's good enough for the average user.
