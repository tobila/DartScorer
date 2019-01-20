load('trainedSVM2.mat')
setup;
% -------------------------------------------------------------------------
% Step 5.3: Evaluate the model on the test data
% -------------------------------------------------------------------------

%im = imread('data/myTestImage.jpg') ;
%im = imread('data/img2_70.jpg') ;
im = imread('../TestImages/left/l_value_15_frame_19.jpg');
im = im2single(im) ;

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
