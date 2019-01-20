run matconvnet/matlab/vl_setupnn ;
run vlfeat/toolbox/vl_setup ;

% % Testbild Links
% im_left = imread('data/l_value_15_frame_19.jpg') ;
% % Testbild Rechts
% im_right = imread('data/r_value_15_frame_19.jpg') ;
% im_left = im2single(im_left) ;
% im_right = im2single(im_right) ;
% 
% homography(im_left, im_right);

%Read all imgs left
D_left = '../TestImages/left/';
S_left = dir(fullfile(D_left,'*.jpg')); % pattern to match filenames.
for k = 1:numel(S_left)
    F = fullfile(D_left,S_left(k).name);
    I = imread(F);
    I = im2single(I);
%     imshow(I)
    S_left(k).data = I; % optional, save data.
end

%Read all imgs right
D_right = '../TestImages/right/';
S_right = dir(fullfile(D_right,'*.jpg')); % pattern to match filenames.
for k = 1:numel(S_right)
    F = fullfile(D_right,S_right(k).name);
    I = imread(F);
    I = im2single(I);
%     imshow(I)
    S_right(k).data = I; % optional, save data.
end


for i = 1:numel(S_right)
   homography(S_left(i).data, S_right(i).data);
   disp('Press a key !')
   pause;
end





