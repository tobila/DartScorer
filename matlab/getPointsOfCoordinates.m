function points = getPointsOfCoordinates(puncturePoint)

% Dartboard Durchmesser=34cm; in Pixel (für 72dpi) = 964px
% 340mm - 964       -> Durchmesser Dartboard
% 1mm - 2,8352941176
% 31,8mm - 90,16    -> Durchmesser SingelBull
% 12,7mm - 36,01    -> Durchmesser Bull
% 8mm - 22,68       -> Breite Double+Tripple Felder
% 107mm - 303,38    -> Abstand äußerer Tripple-Ring
radiusBoard = 964/2;
double = [radiusBoard  radiusBoard-22.68];
single1 = [double(1) 303.38];
tripple = [single1(2) single1(2)-22.68];
single2 = [tripple(2) 45];
singleBull = [single2(2) 18];
bull = [singleBull(2) 0];

boardCenter = [500 500];

% puncturePoint = [300, 200];
pX = puncturePoint(1) - boardCenter(1);
pY = puncturePoint(2) - boardCenter(2);

%keySet = [-9:8 9:26 27:44 45:62 63:80 81:98 99:116 117:134 135:152 153:170 171:180 -179:-172 -171:-154 -153:-136 -135:-118 -117:-100 -99:-82 -81:-64 -63:-46 -45:-28 -27:-10];
keySet = [-81:-64 45:62 81:98 -45:-28 -117:-100 -9:8 117:134 153:170 -153:-136 9:26 171:180 -179:-172 -135:-118 -27:-10 -171:-154 27:44 135:152 63:80 -63:-46 99:116 -99:-82];
valueSet = [];
for i = 1:20
    for k = 1:18
        valueSet = [valueSet, i];
    end
end

% create KeyValuePair from keySet & valueSet
kvp = containers.Map(keySet,valueSet);

% angle as radian
thetaRad = atan2(pY, pX);
%angle in degree
thetaDeg = rad2deg(thetaRad);
%to int:
thetaDeg = fix(thetaDeg);

% distance of puncture point to board center
distance = sqrt(pX^2 + pY^2);


if (distance > radiusBoard)
    points = 0;
elseif ((double(1) > distance) && (distance >= double(2)))
    points = kvp(thetaDeg) * 2;
elseif ((single1(1) > distance) && (distance >= single1(2)))
    points = kvp(thetaDeg);
elseif ((tripple(1) > distance) && (distance >= tripple(2)))
    points = kvp(thetaDeg) * 3;
elseif ((single2(1) > distance) && (distance >= single2(2)))
    points = kvp(thetaDeg);
elseif ((singleBull(1) > distance) && (distance >= singleBull(2)))
    points = 25;
elseif ((bull(1) > distance) && (distance >= bull(2)))
    points = 50;
else
    points = 0;
end


end