run matconvnet/matlab/vl_setupnn ;
run vlfeat/toolbox/vl_setup ;

% Alt
% h2 = [0.9189831800581013 -0.23324956467768873  10.016239187716764;
%     -0.26030894340629473 2.379570039473613 6.874769554642861;
%     -0.0004344898284188348, 0.0011904784866833724 1];
% 
% 
% h1 = [2.362904277747093, 2.2892771513420365, -992.1992397232015;
%     0.5171530192841579, 4.588220913923291, -546.9635124313809;
%     0.0007025318194364153, 0.0023488582342244702, 1];

%Neu
% Links
h2 = [-0.00788306417161418, 0.00326071808604052, -0.255131287988776;
    0.00364802326499404, -0.0209496618961196, -0.966579762813848;
    5.64912385952790e-06,-9.99383444225395e-06,-0.0103255259261100];

% Rechs
h1 = [-0.00184897594639980,-0.00190463022420228,0.853602292907029;
    -0.000609721040552643,-0.00293983913699606,0.520909717269695;
    -7.32006502408362e-07,-1.55610888328265e-06,-0.000362288106181419];


im = imread('data/img2_70.jpg') ;
%im = imread('data/myTestImage.jpg') ;
%im = imread('testImgs/img_15.png') ;

%Testbild Links
% im = imread('data/l_value_15_frame_19.jpg') ;
%Testbild Rechts
%im = imread('data/r_value_15_frame_19.jpg') ;

im = im2single(im) ;


% %RA = imref2d([size(im,1) size(im,2)], [1 size(im,2)], [1 size(im,1)]);
RA = imref2d([1000 1000], [1 1000], [1 1000]);
% 
% 
% t = maketform('projective',h1.');
% imOut = imtransform(im,t);


puncturePoint = getPuncturePoint(im);


tform = projective2d(h2.'); 
imOut = imwarp(im, tform, 'OutputView', RA);
%imOut = imwarp(im, tform);
[x,y] = transformPointsForward(tform,puncturePoint(1),puncturePoint(2));
disp(getPointsOfCoordinates([x,y]));

subplot(1,2,1);
imshow(imOut);
hold on;
plot(x, y, 'r*', 'LineWidth', 2, 'MarkerSize', 5);
   

subplot(1,2,2);
imshow(im);
hold on;
plot(puncturePoint(1), puncturePoint(2), 'r*', 'LineWidth', 2, 'MarkerSize', 5);


