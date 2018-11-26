//#include <opencv2/core/core.hpp>
#include "opencv2/imgproc.hpp"
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <iostream>
#include <string>

using namespace cv;
using namespace std;

Mat maskImagePreprocess(Mat inputImage, Mat mask);
void getCubeColor(Mat cube_square, Mat* color_list, String cube_string, int position);
void getColorRanges(Mat* color_list);

int main( int argc, char** argv ){

	String imageName = "closeTop.jpg";

	Mat bgr_image;
	bgr_image = imread(imageName, 1);

	medianBlur(bgr_image,bgr_image,3);

	Mat hsv_image;
	cvtColor(bgr_image,hsv_image,CV_BGR2HSV);

	String colorString = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB";

	int i=0;

	for(i; i < 54; i++){

		static const unsigned center_piece_vals = (1<<4) | (1<<13) | (1<<22) | (1<<31);

		if((1<<i) & center_piece_vals){ continue; }
		if( i == 40 || i == 49){ continue; } // other center piece values that dont fit in unsigned bits

		String cube_mask;
		cube_mask = "mask" + to_string(i) + ".jpg";
		cout << cube_mask << '\n';

		Mat bw_square;
		bw_square = imread(cube_mask, 0);

	}

	imshow("Image", bgr_image);

  char key = (char) waitKey(0);
  if (key == 'q' || key == 27)
  {
      exit(0);
  }

	return 0;

}

Mat maskImagePreprocess(Mat inputImage, Mat mask){



}

void getCubeColor(Mat cube_square, Mat* color_list, String cube_string, int position){



}

void getColorRanges(Mat* color_list){



}