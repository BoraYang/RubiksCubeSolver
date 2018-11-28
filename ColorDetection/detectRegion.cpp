#include <opencv2/core/core.hpp>
#include "opencv2/imgproc.hpp"
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <iostream>
#include <string>
#include <algorithm>

using namespace cv;
using namespace std;

//Function declarations
int getNonZero(Mat input_array, Mat gray_arr);
string getCubeColor(Mat cube_square, vector<Mat> color_list, string cube_string, int position);
vector<Mat> getColorRanges(vector<Mat> color_list, Mat hsv_image);

int main( int argc, char** argv ){

	Mat bgr_image_ct; bgr_image_ct = imread("closeTop.jpg", 1);
	Mat bgr_image_cb; bgr_image_cb = imread("closeBottom.jpg", 1);
	Mat bgr_image_ft; bgr_image_ft = imread("farTop.jpg", 1);
	Mat bgr_image_fb; bgr_image_fb = imread("farBottom.jpg", 1);

	medianBlur(bgr_image_ct,bgr_image_ct,3);
	medianBlur(bgr_image_cb,bgr_image_cb,3);
	medianBlur(bgr_image_ft,bgr_image_ft,3);
	medianBlur(bgr_image_fb,bgr_image_fb,3);

	Mat hsv_image_ct; cvtColor(bgr_image_ct,hsv_image_ct,CV_BGR2HSV);
	Mat hsv_image_cb; cvtColor(bgr_image_cb,hsv_image_cb,CV_BGR2HSV);
	Mat hsv_image_ft; cvtColor(bgr_image_ft,hsv_image_ft,CV_BGR2HSV);
	Mat hsv_image_fb; cvtColor(bgr_image_fb,hsv_image_fb,CV_BGR2HSV);

	vector<Mat> color_mask_list_top;
	vector<Mat> color_mask_list_bottom; //Need to get hsv values for this
	color_mask_list_top = getColorRanges(color_mask_list_top,hsv_image_ct);

	string colorString = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB";

	int i=0;

	for(i; i < 53; i++){

		//Vector lists for cube mask index used by each image
		vector<int> ct{5,7,8,9,10,11,12,15,19,20,23,26};
		vector<int> cb{18,21,24,25,27,28,29,30,33,41,42,43,44};
		vector<int> ft{0,1,2,3,6,36,37,38,39,45,46,47,50,53};
		vector<int> fb{14,16,17,32,34,35,48,51,52};


		//Center pieces that can be skipped
		if( i == 4 || i == 13 || i == 22 || i == 31 || i == 40 || i == 49){ continue; }

		//Create string for each mask image to open
		String cube_mask;
		cube_mask = "mask" + to_string(i) + ".jpg";

		//Reading in the cube square mask in black and white mode
		Mat bw_square;
		bw_square = imread(cube_mask, 0);

		//Eroding cube square mask to cut out black/white noise on the edge of image
		Mat erode_img;
		Mat element;
		element = getStructuringElement(MORPH_ELLIPSE,Size(9,9),Point(4,4));
		erode(bw_square,erode_img,element);

		Mat img_bw;
		threshold(erode_img, img_bw, 0, 255, CV_THRESH_BINARY | CV_THRESH_OTSU);
		
		Mat cube_square;

		//Figuring out which image to use with the mask
		//imageSet used to short circuit once image has been found.
		bool imageSet = true;
		//Use closeTop.jpg
		if(imageSet && (find(ct.begin(), ct.end(), i) != ct.end())){
			imageSet = false;
			bitwise_and(bgr_image_ct,bgr_image_ct,cube_square,img_bw);
		}
		//Use closeBottom.jpg
		if(imageSet && (find(cb.begin(), cb.end(), i) != cb.end())){
			imageSet = false;
			bitwise_and(bgr_image_cb,bgr_image_cb,cube_square,img_bw);
		}
		//Use farTop.jpg
		if(imageSet && (find(ft.begin(), ft.end(), i) != ft.end())){
			imageSet = false;
			bitwise_and(bgr_image_ft,bgr_image_ft,cube_square,img_bw);
		}
		//Use farBottom.jpg
		if(imageSet && (find(fb.begin(), fb.end(), i) != fb.end())){
			imageSet = false;
			bitwise_and(bgr_image_fb,bgr_image_fb,cube_square,img_bw);
		}

		imshow("Cube Square", cube_square);
		waitKey(0);

		colorString = getCubeColor(cube_square, color_mask_list_top, colorString, i-1);

	}

	cout << colorString << '\n';

	imshow("Image", bgr_image_ct);

	char key = (char) waitKey(0);
	if (key == 'q' || key == 27)
	{
	  exit(0);
	}

	return 0;

}

int getNonZero(Mat input_array, Mat gray_arr){

	int retVal;

	cvtColor(input_array, gray_arr, CV_BGR2GRAY);

	Mat tempArr;
	retVal = countNonZero(gray_arr);

	return retVal;

}

string getCubeColor(Mat cube_square, vector<Mat> color_list, string cube_string, int position){

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

	if (ycount > 200){

		cube_string.replace(position,1,"U");

	}	
	if (bcount > 200){

		cube_string.replace(position,1,"L");

	}
	if (gcount > 200){

		cube_string.replace(position,1,"R");

	}
	if (rcount > 200){

		cube_string.replace(position,1,"F");

	}
	if (ocount > 200){

		cube_string.replace(position,1,"B");

	}
	if (wcount > 200){

		cube_string.replace(position,1,"D");

	}

	return cube_string;

}

/*
	getColorRanges: Sets up the input vector<Mat> color_list with masks
	that represent each color of the cube face. These values will later be
	used to find the color of each cube square mask with a bitwise_and
	computation.
*/
vector<Mat> getColorRanges(vector<Mat> masks, Mat hsv_image){

	Mat mask_yellow; Mat mask_white; Mat mask_blue; Mat mask_green; Mat mask_red; Mat mask_orange;

	inRange(hsv_image,Scalar(26,60,130),Scalar(36,140,190),mask_yellow);
	inRange(hsv_image,Scalar(0,0,160),Scalar(255,50,255),mask_white);
	inRange(hsv_image,Scalar(100,150,0),Scalar(140,255,255),mask_blue);
	inRange(hsv_image,Scalar(50,50,80),Scalar(85,255,255),mask_green);
	inRange(hsv_image,Scalar(0,170,100),Scalar(10,255,160),mask_red);
	inRange(hsv_image,Scalar(5,100,200),Scalar(25,199,255),mask_orange);

	masks.push_back(mask_yellow);
	masks.push_back(mask_white);
	masks.push_back(mask_blue);
	masks.push_back(mask_green);
	masks.push_back(mask_red);
	masks.push_back(mask_orange);

	return masks;

}