% Punkte beginnend zwischen 11 und 14, im Uhrzeigersinn weiter
pts_src = [[186 262];[287 190];[403 131];[526 82];[654 51]; [782 37];[907 43];[1020 72];[1112 125];[1168 201];[1173 305];[1101 429];[945 555];[719 656];[468 698];[256 682];[117 617];[56 530];[58 435];[107 344]]
pts_dst = [[24 425];[71 281];[159 159];[281 71];[425 24];[575 24];[719 71];[841 159];[929 281];[976 425];[976 575];[929 719];[841 841];[719 929];[575 976];[425 976];[281 929];[159 841];[71 719];[24 575]]
src = rot90(pts_src);
src = flip(src)
dst = rot90(pts_dst);
dst = flip(dst)


% im = imread('data/img2_70.jpg') ;
H = homography_solve(src, dst);

% tform = projective2d(H.');
% imOut = imwarp(im, tform);

% subplot(1,2,1);
% imshow(imOut);
   

% subplot(1,2,2);
imshow(im);

% button = 1;
%  while sum(button) <=1   % read ginputs until a mouse right-button occurs
%    [x,y,button] = ginput2(3)
%  end



function v = homography_solve(pin, pout)
% HOMOGRAPHY_SOLVE finds a homography from point pairs
%   V = HOMOGRAPHY_SOLVE(PIN, POUT) takes a 2xN matrix of input vectors and
%   a 2xN matrix of output vectors, and returns the homogeneous
%   transformation matrix that maps the inputs to the outputs, to some
%   approximation if there is noise.
%
%   This uses the SVD method of
%   http://www.robots.ox.ac.uk/%7Evgg/presentations/bmvc97/criminispaper/node3.html
% David Young, University of Sussex, February 2008
if ~isequal(size(pin), size(pout))
    error('Points matrices different sizes');
end
if size(pin, 1) ~= 2
    error('Points matrices must have two rows');
end
n = size(pin, 2);
if n < 4
    error('Need at least 4 matching points');
end
% Solve equations using SVD
x = pout(1, :); y = pout(2,:); X = pin(1,:); Y = pin(2,:);
rows0 = zeros(3, n);
rowsXY = -[X; Y; ones(1,n)];
hx = [rowsXY; rows0; x.*X; x.*Y; x];
hy = [rows0; rowsXY; y.*X; y.*Y; y];
h = [hx hy];
if n == 4
    [U, ~, ~] = svd(h);
else
    [U, ~, ~] = svd(h, 'econ');
end
v = (reshape(U(:,9), 3, 3)).';
end