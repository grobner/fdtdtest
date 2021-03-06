fileID = fopen("data.txt","w");
i = 3;
q = num2str(i);
filename = "P7/" + q + "k" +  ".wav";
    [y,fs] = audioread(filename);
    y = y(:, 1);
    win_len=round(fs*0.5);
    win=MyHanning(win_len);
    fft_size=2^ceil(log2(win_len));
    f = (0:fft_size-1)'*fs/fft_size;
    frame_shift=round(fs*0.5);
    number_of_frames=ceil((length(y)+1)/frame_shift);
    base_index=ceil(-win_len/2):ceil(win_len/2)-1;
    X = zeros(number_of_frames,1);
    F = zeros(number_of_frames,1);
    for j=0:number_of_frames-1
        center=round(j*frame_shift);
        safe_index=max(1,min(length(y),base_index+center));
        tmp=y(safe_index).*win;
        tmpY=20*log10(abs(fft(tmp,fft_size)));
        %plot(f,tmpY);
        ix = round(fft_size*(i*1000)/fs);
        [mx,idx] = max(tmpY(ix-30:ix+30));
        f2 = f(ix-30:ix+30);
        fprintf(fileID,"%s %f %f\n",filename ,f2(idx), mx);
        X(j+1) = mx;
        F(j+1) = f2(idx);
    end
    avex = mean(X);
    avef = mean(F);
    stdx = std(X);
    stdf = std(F);
    fprintf(fileID,"%s %f %f %f %f\n",filename, avef, stdf ,avex,stdx);
    fclose(fileID);
