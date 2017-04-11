M = [1.01 1.05:0.05:1.45 1.5:0.1:1.9 2:0.2:3.8 4:0.5:5 6 8 10 20 40];
bet = 0:0.001:90;
Mn2 = @(Mn1) ((Mn1^2 + (2/0.4))/(2.8/0.4*Mn1^2 - 1))^0.5;
M2 = @(M1,B,Th) Mn2(M1*sind(B))/sind(B-Th);
TBM = @(bet,M) atand(2*cotd(bet).*(M.^2.*sind(bet).^2-1)./(M.^2.*(1.4+cosd(2*bet))+2));

[BB,MM] = meshgrid(bet,M);

thet = TBM(BB,MM);

P = plot(thet,bet,'k');
axis([0 50 0 90])
xlabel('Deflection Angle, \theta (deg)')
ylabel('Shock wave angle, \beta (deg)')
xticklabels = cell(1,101);
xticklabels(1:10:101) = num2cell(0:5:50);
yticklabels = cell(1,91);
yticklabels(1:10:91) = num2cell(0:10:90);
grid on
set(gca,'XTick',0:0.5:51,'XTickLabel',xticklabels,...
    'YTick',0:90,'YTickLabel',yticklabels,'GridLineStyle','-')

[v,i] = max(thet,[],2);
for j = 1:length(v)
    bb = bet(i(j));
    tt = v(j);
    m2 = M2(M(j),bb,tt);
    while m2<1
        bb = bb - 0.2;
        tt = TBM(bb,M(j));
        m2 = M2(M(j),bb,tt);
    end
    tmin(j) = tt;
    bmin(j) = bb;
end
b = bet(i(2:end));
b(end) = b(end) + 1.25;
T1 = text(v(2:end),b+2,num2cell(M(2:end)));
set(T1,'BackgroundColor','w','Margin',0.00001,'FontSize',5.5)
T2 = text([TBM(82,M(end)) TBM(41,M(end))],[85 37],{'Strong Shock, M_2<1','Weak Shock, M_2>1'});
set(T2,'BackgroundColor','w','Margin',0.00001)
set(T2(1),'Rotation',-12.5)
set(T2(2),'Rotation',27.5)
hold on
maxth = plot(v,bet(i),'k','LineWidth',2);
m1 = plot(tmin,bmin,'k--','LineWidth',2);
hold off
legend([maxth,m1],'\theta=\theta_{max}','M_2=1')
h=gcf;
set(h,'PaperPositionMode','auto'); 
set(h,'Position',[50 50 1200 800]);
set(h,'PaperOrientation','landscape');
print(gcf, '-dpdf', 'TBM.pdf')


