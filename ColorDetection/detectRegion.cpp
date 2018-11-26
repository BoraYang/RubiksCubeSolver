#include <opencv2/core/core.hpp>
#include "opencv2/imgproc.hpp"
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <iostream>
#include <string>

using namespace cv;
using namespace std;

//Function declarations
Mat maskImagePreprocess(Mat inputImage, Mat mask);
void getCubeColor(Mat cube_square, vector<Mat> color_list, String cube_string, int position);
void getColorRanges(vector<Mat> color_list, Mat hsv_image);

int main( int argc, char** argv ){

	Mat bgr_image;
	bgr_image = imread("closeTop.jpg", 1);

	medianBlur(bgr_image,bgr_image,3);

	Mat hsv_image;
	cvtColor(bgr_image,hsv_image,CV_BGR2HSV);

	vector<Mat> color_mask_list;
	getColorRanges(color_mask_list,hsv_image);

	String colorString = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB";

	int i=0;

	for(i; i < 18; i++){

		//Used to bit mask positions of i that are center pieces --> skip centers
		static const unsigned center_piece_vals = (1<<0) | (1<<5) | (1<<7) |(1<<14) | (1<<22) | (1<<31);

		//Skips center pieces (values in cube string for center pieces are already set)
		if((1<<i) & center_piece_vals){ continue; }
		if( i == 40 || i == 49){ continue; } // other center piece values that dont fit in unsigned bits

		//Create string for each mask image to open
		String cube_mask;
		cube_mask = "mask" + to_string(i) + ".jpg";
		cout << cube_mask << '\n';

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
		bitwise_and(bgr_image,bgr_image,cube_square,img_bw);

		imshow("Cube Square", cube_square);
		waitKey(0);

		//getCubeColor(cube_square, color_mask_list, colorString, i);

	}

	imshow("Image", bgr_image);

	char key = (char) waitKey(0);
	if (key == 'q' || key == 27)
	{
	  exit(0);
	}

	return 0;

}

void getCubeColor(Mat cube_square, vector<Mat> color_list, String cube_string, int position){



}

/*
	getColorRanges: Sets up the input vector<Mat> color_list with masks
	that represent each color of the cube face. These values will later be
	used to find the color of each cube square mask with a bitwise_and
	computation.
*/
void getColorRanges(vector<Mat> color_list, Mat hsv_image){

	Mat mask_yellow;
	Mat mask_white;
	Mat mask_blue;
	Mat mask_green;
	Mat mask_red;
	Mat mask_orange;

	inRange(hsv_image,Scalar(26,60,130),Scalar(36,140,190),mask_yellow);
	inRange(hsv_image,Scalar(0,0,160),Scalar(255,50,255),mask_white);
	inRange(hsv_image,Scalar(100,150,0),Scalar(140,255,255),mask_blue);
	inRange(hsv_image,Scalar(50,50,80),Scalar(85,255,255),mask_green);
	inRange(hsv_image,Scalar(0,170,100),Scalar(10,255,160),mask_red);
	inRange(hsv_image,Scalar(5,100,200),Scalar(25,199,255),mask_orange);

	color_list.push_back(mask_yellow);
	color_list.push_back(mask_white);
	color_list.push_back(mask_blue);
	color_list.push_back(mask_green);
	color_list.push_back(mask_red);
	color_list.push_back(mask_orange);

}