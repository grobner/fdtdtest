fileID = fopen("data.txt","w"); 
zatu = zeros(4); 
for i = 1 : 20 
    q = num2str(i);
    filename = q + "k" +  ".wav";
    [~,fs] = audioread(filename);
    samples = [1,2*fs]; 
    clear y fs;
    [y,fs] = audioread(filename,samples); 
    n = size(y); 
    n = n(1); 
    t = 0:n-1; 
    t = t/fs; 
    yfft = abs(fft(y));
    yfft = yfft.^2;
    yfft = yfft(1:n/2,1);
    f = (0:n/2-1)'*fs/n; 
    ix = round(n*(i*1000)/fs);
    [mx,idx] = max(yfft(ix-30:ix+30)); 
    f2 = f(ix-30:ix+30);
    fprintf(fileID,"%s %f %f\n",filename ,f2(idx), mx);
    %plot(f,yfft,"o-"); 
    %xlim([0 fs/2]);     
    %xlabel("Frequency (Hz)");
    %ylabel("Power")
end
fclose(fileID);