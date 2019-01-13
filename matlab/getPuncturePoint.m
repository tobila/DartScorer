function p = getPuncturePoint(im)

load('trainedSVM.mat');
% load('trainedSVM2.mat');

% im = imread('data/img2_70.jpg') ;
% im = imread('testImgs/cam2/dart_20.png') ;
%  im = im2single(im) ;

%Testbild Links
%im = imread('data/l_value_15_frame_19.jpg') ;

% Compute detections
[detections, scores] = detect(im, w, hogCellSize, scales) ;
keep = boxsuppress(detections, scores, 0.25) ;
detections = detections(:, keep(1:10)) ;
scores = scores(keep(1:10)) ;

cX = (detections(1,1) + detections(3,1))/2;
cY = (detections(2,1) + detections(4,1))/2;

% Plot top detection
figure(3) ; clf ;
imagesc(im) ; axis equal ;
hold on ;
vl_plotbox(detections, 'g', 'linewidth', 2, ...
  'label', arrayfun(@(x)sprintf('%.2f',x),scores,'uniformoutput',0)) ;
title('Multiple detections') ;
plot(cX, cY, 'r*', 'LineWidth', 2, 'MarkerSize', 5);
% 
p = [cX cY];
end