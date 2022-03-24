%['General trash', 'Paper', 'Paper pack', 'Metal', 'Glass', 'Plastic', 'Styrofoam', 'Plastic bag', 'Battery', 'Clothing']
energy_map=load('C:\Users\KimTaeHa\Desktop\boostcamp AI Tech\Basic Assign & Code example\Code-example 220321\EDA\energy_map_class8.txt');
point_map=load('C:\Users\KimTaeHa\Desktop\boostcamp AI Tech\Basic Assign & Code example\Code-example 220321\EDA\point_map_class8.txt');
energy_map = energy_map./max(energy_map(:));
point_map = point_map./max(point_map(:));
%norm_EMap = exp((energy_map-mean(energy_map(:))).^2/std(energy_map(:))^2)/(std(energy_map(:))*sqrt(2*pi));
%norm_PMap = exp((point_map-mean(point_map(:))).^2/std(point_map(:))^2)/(std(point_map(:))*sqrt(2*pi));
figure,
subplot(1,2,1); imshow(energy_map./max(energy_map(:)));
subplot(1,2,2); imshow(point_map./max(point_map(:)));
%subplot(2,3,4); imshow(norm_EMap);
%subplot(2,3,5); imshow(norm_PMap);