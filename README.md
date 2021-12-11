# API OCR 

This is an application that uses cloudmersive api rest service to detect caracters in images OCR. The process receives a url from aws s3 that corresponds to an image of an engine plate. The image is captured and processed through cloudmersive ocr. The result obtained (resulting image and json with recognized word data) is stored in aws s3 and returned to the user.

The project implements an api rest server, using Flask, to allow that the algorithm to be consumed from any application. 