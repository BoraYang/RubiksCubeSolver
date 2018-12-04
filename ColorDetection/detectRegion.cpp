//TODO: Fix red/orange color values and fix bottom color thresholds
// a little bit to better detect.

#include <opencv2/core/core.hpp>
#include "opencv2/imgproc.hpp"
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace cv;
using namespace std;

//Function declarations
void getImageFromCamera(Mat &bgr_input, int cameraIndex);
int getNonZero(Mat input_array, Mat gray_arr);
void getCubeColor(Mat cube_square, vector<Mat> color_list, string &cube_string, int position);
void setupLowMask(vector<Mat> &color_list, Mat hsv_image);
void setupHighMask(vector<Mat> &color_list, Mat hsv_image);

int main( int argc, char** argv ){

	//Color images for each camera
	// Mat bgr_image_ct; bgr_image_ct = imread("closeTop.jpg", 1);
	// Mat bgr_image_cb; bgr_image_cb = imread("closeBottom.jpg", 1);
	// Mat bgr_image_ft; bgr_image_ft = imread("farTop.jpg", 1);
	// Mat bgr_image_fb; bgr_image_fb = imread("farBottom.jpg", 1);

	Mat bgr_image_ct; getImageFromCamera(bgr_image_ct, 3);
	Mat bgr_image_cb; getImageFromCamera(bgr_image_cb, 2);
	Mat bgr_image_ft; getImageFromCamera(bgr_image_ft, 1);
	Mat bgr_image_fb; getImageFromCamera(bgr_image_fb, 0);

	medianBlur(bgr_image_ct,bgr_image_ct,3);
	medianBlur(bgr_image_cb,bgr_image_cb,3);
	medianBlur(bgr_image_ft,bgr_image_ft,3);
	medianBlur(bgr_image_fb,bgr_image_fb,3);

	Mat hsv_image_ct; cvtColor(bgr_image_ct,hsv_image_ct,CV_BGR2HSV);
	Mat hsv_image_cb; cvtColor(bgr_image_cb,hsv_image_cb,CV_BGR2HSV);
	Mat hsv_image_ft; cvtColor(bgr_image_ft,hsv_image_ft,CV_BGR2HSV);
	Mat hsv_image_fb; cvtColor(bgr_image_fb,hsv_image_fb,CV_BGR2HSV);

	vector<Mat> mask_list_ct; setupHighMask(mask_list_ct, hsv_image_ct);
	vector<Mat> mask_list_cb; setupLowMask(mask_list_cb, hsv_image_cb);
	vector<Mat> mask_list_ft; setupHighMask(mask_list_ft, hsv_image_ft);
	vector<Mat> mask_list_fb; setupLowMask(mask_list_fb, hsv_image_fb);

	string colorString = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB";

	//Masks per image
	vector<int> ct{5,7,8,9,10,11,12,15,19,20,23,26};
	vector<int> cb{18,21,24,25,27,28,29,30,33,41,42,43,44};
	vector<int> ft{0,1,2,3,6,36,37,38,39,45,46,47,50,53};
	vector<int> fb{14,16,17,32,34,35,48,51,52};

	int i=0;

	for(i; i < ct.size(); i++){

		string cube_mask;
		cube_mask = "mask" + to_string(ct.at(i)) + ".jpg";

		//Reading in the cube square mask in black and white mode
		Mat bw_square;
		bw_square = imread(cube_mask, 0);

		//Eroding cube square mask to cut out black/white noise on the edge of image
		Mat erode_img;
		Mat element;
		element = getStructuringElement(MORPH_ELLIPSE,Size(20,20),Point(8,8));
		erode(bw_square,erode_img,element);

		Mat img_bw;
		threshold(erode_img, img_bw, 0, 255, CV_THRESH_BINARY | CV_THRESH_OTSU);
		
		Mat cube_square;
		bitwise_and(bgr_image_ct,bgr_image_ct,cube_square,img_bw);

		getCubeColor(cube_square, mask_list_ct, colorString, ct.at(i));

		imshow("cube", cube_square);
		waitKey(0);
	}

	i=0;
	for(i; i < cb.size(); i++){

		string cube_mask;
		cube_mask = "mask" + to_string(cb.at(i)) + ".jpg";

		//Reading in the cube square mask in black and white mode
		Mat bw_square;
		bw_square = imread(cube_mask, 0);

		//Eroding cube square mask to cut out black/white noise on the edge of image
		Mat erode_img;
		Mat element;
		element = getStructuringElement(MORPH_ELLIPSE,Size(20,20),Point(8,8));
		erode(bw_square,erode_img,element);

		Mat img_bw;
		threshold(erode_img, img_bw, 0, 255, CV_THRESH_BINARY | CV_THRESH_OTSU);
		
		Mat cube_square;
		bitwise_and(bgr_image_cb,bgr_image_cb,cube_square,img_bw);

		getCubeColor(cube_square, mask_list_cb, colorString, cb.at(i));

		imshow("cube", cube_square);
		waitKey(0);

	}

	i=0;
	for(i; i < ft.size(); i++){

		string cube_mask;
		cube_mask = "mask" + to_string(ft.at(i)) + ".jpg";

		//Reading in the cube square mask in black and white mode
		Mat bw_square;
		bw_square = imread(cube_mask, 0);

		//Eroding cube square mask to cut out black/white noise on the edge of image
		Mat erode_img;
		Mat element;
		element = getStructuringElement(MORPH_ELLIPSE,Size(20,20),Point(8,8));
		erode(bw_square,erode_img,element);

		Mat img_bw;
		threshold(erode_img, img_bw, 0, 255, CV_THRESH_BINARY | CV_THRESH_OTSU);
		
		Mat cube_square;
		bitwise_and(bgr_image_ft,bgr_image_ft,cube_square,img_bw);

		getCubeColor(cube_square, mask_list_ft, colorString, ft.at(i));

		imshow("cube", cube_square);
		waitKey(0);

	}

	i=0;
	for(i; i < fb.size(); i++){

		string cube_mask;
		cube_mask = "mask" + to_string(fb.at(i)) + ".jpg";

		//Reading in the cube square mask in black and white mode
		Mat bw_square;
		bw_square = imread(cube_mask, 0);

		//Eroding cube square mask to cut out black/white noise on the edge of image
		Mat erode_img;
		Mat element;
		element = getStructuringElement(MORPH_ELLIPSE,Size(20,20),Point(8,8));
		erode(bw_square,erode_img,element);

		Mat img_bw;
		threshold(erode_img, img_bw, 0, 255, CV_THRESH_BINARY | CV_THRESH_OTSU);
		
		Mat cube_square;
		bitwise_and(bgr_image_fb,bgr_image_fb,cube_square,img_bw);

		getCubeColor(cube_square, mask_list_fb, colorString, fb.at(i));

		imshow("cube", cube_square);
		waitKey(0);

	}

	ofstream myFile;
	const char *path = "/home/reed/RubiksCubeSolver/solution.txt";
	myFile.open(path);

	myFile << colorString;

	myFile.close();

	return 0;

}

void getImageFromCamera(Mat &bgr_input, int cameraIndex){

	VideoCapture cap(cameraIndex);

	if(!cap.isOpened()){
		cout << "Camera " << cameraIndex << " cannot be opened. Please check that it is connected properly.";
		exit(1);
	}

	cap >> bgr_input;

}

int getNonZero(Mat input_array, Mat gray_arr){

	int retVal;

	cvtColor(input_array, gray_arr, CV_BGR2GRAY);

	Mat tempArr;
	retVal = countNonZero(gray_arr);

	return retVal;

}

void getCubeColor(Mat cube_square, vector<Mat> color_list, string &cube_string, int position){

	//Yellow: 0, White: 1, Blue: 2, Green: 3, Red: 4, Orange: 5
  	//Yellow: U, White: D, Blue: L, Green: R, Red: F, Orange: B

	Mat yellow; Mat white; Mat blue; Mat green; Mat red; Mat orange;
	Mat gY; Mat gW; Mat gB; Mat gG; Mat gR; Mat gO;
	int ycount; int wcount;int bcount; int gcount; int rcount; int ocount;

	bitwise_and(cube_square,cube_square,yellow, color_list.at(0));
	bitwise_and(cube_square,cube_square,white, color_list.at(1));
	bitwise_and(cube_square,cube_square,blue, color_list.at(2));
	bitwise_and(cube_square,cube_square,green, color_list.at(3));
	bitwise_and(cube_square,cube_square,red, color_list.at(4));
	bitwise_and(cube_square,cube_square,orange, color_list.at(5));

	ycount = getNonZero(yellow, gY);
	wcount = getNonZero(white, gW);
	bcount = getNonZero(blue, gB);
	gcount = getNonZero(green, gG);
	rcount = getNonZero(red, gR);
	ocount = getNonZero(orange, gO);
	int diff = rcount - ocount;

	printf("%d Y:%d, W:%d, B:%d, G:%d, R:%d, O:%d\n", position, ycount, wcount, bcount, gcount, rcount, ocount);

	if (ycount > 400){

		cube_string.replace(position,1,"U");
		return;
	}	
	if (bcount > 400){

		cube_string.replace(position,1,"L");
		return;
	}
	if (gcount > 400){

		cube_string.replace(position,1,"R");
		return;
	}
	if (wcount > 400){

		cube_string.replace(position,1,"D");
		return;
	}
	if (diff > 60){

		cube_string.replace(position,1,"F");
		return;
	}
	else{

		cube_string.replace(position,1,"B");
		return;
	}

}

/*
	getColorRanges: Sets up the input vector<Mat> color_list with masks
	that represent each color of the cube face. These values will later be
	used to find the color of each cube square mask with a bitwise_and
	computation.
*/
void setupHighMask(vector<Mat> &masks, Mat hsv_image){

	Mat mask_yellow; Mat mask_white; Mat mask_blue; Mat mask_green; Mat mask_red; Mat mask_orange;

	inRange(hsv_image,Scalar(26,40,55),Scalar(40,255,255),mask_yellow);
	inRange(hsv_image,Scalar(0,0,0),Scalar(255,50,255),mask_white);
	inRange(hsv_image,Scalar(100,100,0),Scalar(140,255,255),mask_blue);
	inRange(hsv_image,Scalar(50,50,0),Scalar(85,255,255),mask_green);
	inRange(hsv_image,Scalar(0,50,0),Scalar(10,255,255),mask_red);
	inRange(hsv_image,Scalar(5,50,50),Scalar(25,255,255),mask_orange);

	masks.push_back(mask_yellow);
	masks.push_back(mask_white);
	masks.push_back(mask_blue);
	masks.push_back(mask_green);
	masks.push_back(mask_red);
	masks.push_back(mask_orange);

}

void setupLowMask(vector<Mat> &masks, Mat hsv_image){

	Mat mask_yellow; Mat mask_white; Mat mask_blue; Mat mask_green; Mat mask_red; Mat mask_orange;

	inRange(hsv_image,Scalar(26,40,100),Scalar(40,255,255),mask_yellow);
	inRange(hsv_image,Scalar(0,0,0),Scalar(255,90,255),mask_white);
	inRange(hsv_image,Scalar(100,100,0),Scalar(140,255,255),mask_blue);
	inRange(hsv_image,Scalar(41,50,35),Scalar(85,255,255),mask_green);
	inRange(hsv_image,Scalar(0,140,20),Scalar(10,240,255),mask_red);
	inRange(hsv_image,Scalar(5,50,50),Scalar(25,255,255),mask_orange);

	masks.push_back(mask_yellow);
	masks.push_back(mask_white);
	masks.push_back(mask_blue);
	masks.push_back(mask_green);
	masks.push_back(mask_red);
	masks.push_back(mask_orange);

}