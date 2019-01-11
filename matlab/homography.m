run matconvnet/matlab/vl_setupnn ;
run vlfeat/toolbox/vl_setup ;

h2 = [0.9189831800581013 -0.23324956467768873  10.016239187716764;
    -0.26030894340629473 2.379570039473613 6.874769554642861;
    -0.0004344898284188348, 0.0011904784866833724 1];


h1 = [2.362904277747093, 2.2892771513420365, -992.1992397232015;
    0.5171530192841579, 4.588220913923291, -546.9635124313809;
    0.0007025318194364153, 0.0023488582342244702, 1];



im = imread('data/img2_70.jpg') ;
%im = imread('data/myTestImage.jpg') ;
%im = imread('testImgs/img_15.png') ;
im = im2single(im) ;


% %RA = imref2d([size(im,1) size(im,2)], [1 size(im,2)], [1 size(im,1)]);
RA = imref2d([1000 1000], [1 1000], [1 1000]);
% 
% 
% t = maketform('projective',h1.');
% imOut = imtransform(im,t);


puncturePoint = getPuncturePoint(im);


tform = projective2d(h1.'); 
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


