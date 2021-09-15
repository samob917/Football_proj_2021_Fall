choices_o = [];
%buckets: 1-10, 11-22, 23-29
%pick 3 from each bucket, for each of 5 seasons (2015,2016,2017,2018,2019)
%do the same for defense
for i = 1:5
    sample1 = 1:10;
    sample2 = 11:22;
    sample3 = 23:32;
    
    a = randsample(sample1,3);
    b = randsample(sample2, 3);
    c = randsample(sample3, 3);
    choices_o = [choices_o, a, b, c];
end
choices_o
choices_d = [];
for i = 1:5
    sample1 = 1:10;
    sample2 = 11:22;
    sample3 = 23:32;
    
    a = randsample(sample1,3);
    b = randsample(sample2, 3);
    c = randsample(sample3, 3);
    choices_d = [choices_d, a, b, c];
end

choices_d