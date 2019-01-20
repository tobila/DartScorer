function homography(im_left, im_right)

% Links
h_left = [-0.00788306417161418, 0.00326071808604052, -0.255131287988776;
    0.00364802326499404, -0.0209496618961196, -0.966579762813848;
    5.64912385952790e-06,-9.99383444225395e-06,-0.0103255259261100];

% Rechs
h_right = [-0.00184897594639980,-0.00190463022420228,0.853602292907029;
    -0.000609721040552643,-0.00293983913699606,0.520909717269695;
    -7.32006502408362e-07,-1.55610888328265e-06,-0.000362288106181419];


%im = imread('data/img2_70.jpg') ;
%im = imread('data/myTestImage.jpg') ;
%im = imread('testImgs/img_15.png') ;

%Testbild Links
%im = imread('data/l_value_15_frame_19.jpg') ;
%Testbild Rechts
% im = imread('data/r_value_15_frame_19.jpg') ;
% 
% im = im2single(im) ;


puncturePoint_left = getPuncturePoint(im_left, "left");
puncturePoint_right = getPuncturePoint(im_right, "right");


RA = imref2d([1000 1000], [1 1000], [1 1000]);
tform_left = projective2d(h_left.'); 
tform_right = projective2d(h_right.'); 

imOut_left = imwarp(im_left, tform_left, 'OutputView', RA);
imOut_right = imwarp(im_right, tform_right, 'OutputView', RA);
%imOut = imwarp(im, tform);
[x_left,y_left] = transformPointsForward(tform_left,puncturePoint_left(1),puncturePoint_left(2));
[x_right,y_right] = transformPointsForward(tform_right,puncturePoint_right(1),puncturePoint_right(2));
disp(getPointsOfCoordinates([x_left,y_left]));
disp(getPointsOfCoordinates([x_right,y_right]));


figure(1) ; clf ;
subplot(2,2,1);
imshow(imOut_left);
hold on;
plot(x_left, y_left, 'r*', 'LineWidth', 2, 'MarkerSize', 5);
   

subplot(2,2,2);
imshow(im_left);
hold on;
plot(puncturePoint_left(1), puncturePoint_left(2), 'r*', 'LineWidth', 2, 'MarkerSize', 5);


subplot(2,2,3);
imshow(imOut_right);
hold on;
plot(x_right, y_right, 'r*', 'LineWidth', 2, 'MarkerSize', 5);
   

subplot(2,2,4);
imshow(im_right);
hold on;
plot(puncturePoint_right(1), puncturePoint_right(2), 'r*', 'LineWidth', 2, 'MarkerSize', 5);


