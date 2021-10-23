pragma foreign_key=on;

--创建学生表：学号 姓名 专业 班级 性别 出生日期 电话号码 宿舍楼 宿舍号 家庭住址
create table student(
sno char(9) not null primary key,
sname varchar(20) not null unique,
major varchar(30) not null,
class varchar(10) not null,
sgender char(2) not null,
birthday  datetime not null,
stelephone varchar(11) not null,
dorm int(2) not null,
dormnum int(3) not null,
liveplace varchar(40) not null
);

--创建教师表：工号 姓名 性别 电话号码 职务
create table teacher(
tno char(9) not null primary key,
tname varchar(20) not null unique,
tgender char(2) not null,
ttelephone varchar(11) not null,
tcareer varchar(10) not null
);

--创建三二一师生关系表 老师姓名 工号 老师电话 学生姓名 学号 学生电话 学生家长姓名 学生家长电话 是否为重点关注对象
create table relative( 
tname varchar(20) not null,
tno char(9) not null,
ttelephone varchar(11) not null,
sname varchar(20) not null,
sno char(9) not null,
stelephone varchar(11) not null,
spname varchar(20) not null,
sptelephone varchar(11) not null,
attention char(2) not null,
primary key(tno,sno),
foreign key(tname) references teacher(tname),
foreign key(tno) references teacher(tno),
foreign key(ttelephone) references teacher(ttelephone),
foreign key(sname) references student(sname),
foreign key(sno) references student(sno),
foreign key(stelephone) references student(stelephone)
);

--创建三二一活动记录表 老师工号 姓名 与学生三二一活动次数
create table calculate(
tno char(9) not null primary key,
tname varchar(20) not null unique,
acnumber char(3),
foreign key(tno) references teacher(tno),
foreign key(tname) references teacher(tname)
);

--插入学生表数据：
insert into student values('220163321','那孜衣拉·赛力克','信息管理与信息系统','信管161','女','1998/1/1','16699218020',3,432,'新疆乌鲁木齐市头屯河区万泰阳光城二期62号楼');
insert into student values('220163331','祖丽皮亚木·阿不都瓦力','信息管理与信息系统','信管162','女','1998/1/28','17881123965',3,432,'新疆呼图壁县芳草湖镇团结北路232号');
insert into student values('220163332','古力米拉·如孜','信息管理与信息系统','信管171','女','1999/2/12','18199461551',12,423,'新疆霍城县清水河镇开封路南2巷11号');
insert into student values('220163334','阿吉古力·米吉提','信息管理与信息系统','信管172','女','1999/2/21','15899465955',3,425.'新疆特克斯县乔拉克铁热克镇乌尊布拉克路八巷22号');
insert into student values('220163335','古丽巴哈尔·库尔班','信息管理与信息系统','信管181','女','2000/3/14','15292532758',12,427,'新疆省乌苏市皇宫镇西海子村250号');

insert into student values('220163349','阿热孜古力·巴拉提','计算机科学与技术','计科171','女','1999/8/11','13279720779',12,423,'新疆奎屯市柳沟125团兴隆里1栋161号');
insert into student values('220163350','吾尔尼沙·吐逊','计算机科学与技术','计科172','女','1999/8/24','18599013480',3,426,'新疆乌鲁木齐市天山区1195号');
insert into student values('220163352','阿曼尼沙·托合提','计算机科学与技术','计科174','女','1999/9/18','13809949757',12,427,'甘肃省永登县中堡镇清水河村三社');
insert into student values('220163353','帕沙姑丽·阿布力米提','计算机科学与技术','计科175','女','1999/9/19','13579878402',3,425,'新疆昭苏县阔克吐拜镇77团丁香路1号楼4单元402室');
insert into student values('220163356','吐尔逊姑丽·艾木都拉','计算机科学与技术','计科171','女','1999/5/23','17881121322',12,429,'新疆阿勒泰市富蕴县吐尔洪乡阔仔肯村52号');

insert into student values('220190408','姜雨航','物联网工程','物联192','男','2001/8/8','15696744086',6,202,'重庆市垫江县五洞镇文龙村5组');
insert into student values('220190409','刘丹','物联网工程','物联161','女','1998/12/31','13320363122',12,334,'重庆市垫江县杠家镇双溪2组二十号');
insert into student values('220190410','谭治强','物联网工程','物联162','男','1998/12/31','13272722840',6,203,'重庆市开州区岳溪镇石坪村9组77号');
insert into student values('220190412','翁建明','物联网工程','物联171','男','1999/1/2','15608021662',6,332,'四川省安岳县千佛乡桥亭村');
insert into student values('220190413','张海洋','物联网工程','物联172','男','1999/1/17','15099585532',6,334,'四川省梓潼县文昌镇五丁路北段233号');

insert into student values('220190416','吕朋辉','电子信息科学与技术','电科161','男','1998/9/15','17808243601',6,204,'四川省大英县蓬莱镇碑垭村10社23号');
insert into student values('220190418','鞠直成','电子信息科学与技术','电科162','男','1998/9/23','17628330168',6,336,'四川省乐山市沐川县永福镇永兴村3组10号');
insert into student values('220190419','雷鑫','电子信息科学与技术','电科171','男','1999/10/17','18582813701',6,336,'四川渠县李馥乡真武村三组1号');
insert into student values('220190420','李奇峰','电子信息科学与技术','电科172','男','1999/10/18','18382713299',6,205,'将军大道24号南林山庄2幢3单元201室');
insert into student values('220190421','苟玉鲜','电子信息科学与技术','电科181','男','2000/6/19','15082714268',6,205,'四川省巴中市平昌县灵山乡民意村11社');
insert into student values('220163341','努尔比耶姆·图尔荪','信息管理与信息系统','信管162','女','1998/5/21','15160896514',3,425,'新疆温宿县依希来木其乡团结村2组253号');				

insert into student values('220163359','美合日·托合提麦麦提','计算机科学与技术','计科191','女','2001/12/22','17881127509',12,423,'新疆新源县阿勒玛勒乡铁勒喀拉村巴彦德路十二巷6号');
insert into student values('220163358','麦热耶·拜克尔','计算机科学与技术','计科181','女','2000/4/21','15276833340',3,429,'新疆喀什地区喀什市英吾斯坦乡');
insert into student values('220190431','付柳婷','电子信息科学与技术','电科191','女','2001/11/21','18009933660',12,335,'新疆石河子市21小区8栋122');
insert into student values('220190429','李傲','电子信息科学与技术','电科191','男','2001/7/19','13079972246',6,204,'河南省平舆县射桥古城后柴楼村');
insert into student values('220190415','张濒方','物联网工程','物联192','男','2001/9/5','18508390091',6,334,'四川省广元市苍溪县石马镇千佛村三组32号');	

--插入老师表数据:
insert into teacher values('120010043','蔡朝朝','女','15352517720','干部教师');
insert into teacher values('120010041','李湘','女','13999917205','干部教师');
insert into teacher values('120190008','王晓东','男','15276710090','团委书记');
insert into teacher values('120020025','杨抒','男','13999913640','副院长');
insert into teacher values('119850032','金晓龙','男','18690190015','党委书记');
insert into teacher values('120160018','阿迪力','男','13999187347','辅导员');
insert into teacher values('119970034','冯向萍','女','13579200192','副院长');
insert into teacher values('119900028','张太红','男','13325538255','院长');

--插入关系表数据:
insert into relative values('蔡朝朝','120010043','15352517720','那孜衣拉·赛力克','220163321','16699218020','赛力克·木哈提','15999255384','是');
insert into relative values('蔡朝朝','120010043','15352517720','祖丽皮亚木·阿不都瓦力','220163331'	,'17881123965','阿不都瓦力·阿不拉','13239978179','是');
insert into relative values('蔡朝朝','120010043','15352517720','古力米拉·如孜','220163332','18199461551','如孜·阿不拉','18196376818','是');
insert into relative values('李湘','120010041','13999917205','阿吉古力·米吉提','220163334','15899465955','米吉提·日西提','13139868821','是');
insert into relative values('李湘','120010041','13999917205','阿热孜古力·巴拉提','220163349','13279720779','巴拉提·艾买提','17799544076','是');
insert into relative values('李湘','120010041','13999917205','吾尔尼沙·吐逊','220163350','18599013480','古力那尔·巴拉提','15599849866','是');
insert into relative values('李湘','120010041','13999917205','阿曼尼沙·托合提','220163352','13809949757','托合提·买合苏提','15739964926','是');
insert into relative values('王晓东','120190008','15276710090','帕沙姑丽·阿布力米提','220163353','13579878402','阿布力米提·苏来曼','13779725409','是');
insert into relative values('王晓东','120190008','15276710090','吐尔逊姑丽·艾木都拉','220163356','17881121322','艾木都拉·阿布拉','19999282868','是');
insert into relative values('杨抒','120020025','13999913640','姜雨航','220190408','15696744086','吴小琼','13108661836','否');
insert into relative values('杨抒','120020025','13999913640','刘丹','220190409','13320363122','刘士汉','15059837630','否');
insert into relative values('杨抒','120020025','13999913640','谭治强','220190410','13272722840','谭世明','13650373478','否');
insert into relative values('杨抒','120020025','13999913640','翁建明','220190412','15608021662','翁绍武','13458666358','否');
insert into relative values('杨抒','120020025','13999913640','张海洋','220190413','15099585532','张冬梅','15882856368','否');
insert into relative values('金晓龙','119850032','18690190015','吕朋辉','220190416','17808243601','吕维兵','19961085714','否');
insert into relative values('金晓龙','119850032','18690190015','鞠直成','220190418','17628330168','鞠远伦','13990630721','否');
insert into relative values('金晓龙','119850032','18690190015','雷鑫','220190419','18582813701','江文惠','18228675792','否');
insert into relative values('阿迪力','120160018','13999187347','李奇峰','220190420','18382713299','宋国英','18382796710','否');
insert into relative values('阿迪力','120160018','13999187347','苟玉鲜','220190421','15082714268','吴蓉珍','18728747056','否');
insert into relative values('阿迪力','120160018','13999187347','美合日·托合提麦麦提','220163359','17881127509','托合提麦麦提·佧马力','15214924947','是');
insert into relative values('阿迪力','120160018','13999187347','麦热耶·拜克尔','220163358','15276833340','拜克尔·托合图木尔','15276000464','是');
insert into relative values('冯向萍','119970034','13579200192','付柳婷','220190431','18009933660','付国华','18009936665','否');
insert into relative values('冯向萍','119970034','13579200192','李傲','220190429','13079972246','李国宾','13629901239','否');
insert into relative values('冯向萍','119970034','13579200192','张濒方','220190415','18508390091','张毅','13780130570','否');

--插入统计表数据:老师工号 姓名 与学生三二一活动次数
insert into calculate values('120010043','蔡朝朝',10);
insert into calculate values('120010041','李湘',7);
insert into calculate values('120190008','王晓东',5);
insert into calculate values('120020025','杨抒',4);
insert into calculate values('119850032','金晓龙',14);
insert into calculate values('120160018','阿迪力',9);

--创建触发器：一旦删除三二一师生关系的学生信息，学生表也会删除学生信息
create trigger tr after delete 
on relative for each row 
begin
delete from student where sno = old.sno; 
end;
--创建触发器：一旦删除三二一师生关系的学生信息，学生表也会删除学生信息
create trigger tr1 after delete
on relative for each row
begin
delete from student where sname = old.sname; 
end;
--创建触发器：一旦修改学生表信息-电话号码，三二一师生表也会修改学生信息
create trigger tr2 after update
on student for each row 
begin
update relative set stelephone = new.stelephone where stelephone = old.stelephone;
end;
--创建触发器：一旦修改教师表信息-电话号码，三二一师生表也会修改教师信息
create trigger tr3 after update 
on teacher for each row 
begin 
update relative set ttelephone = new.ttelephone where ttelephone = old.ttelephone;
end;

--创建视图：用于查看学生信息
create view view_studentinfo
as
select student.sno,sname,class,stelephone,dorm,dormnum,sptelephone
from student join relative on student.sno=relative.sno;

--创建视图：用于查看教师信息
create view view_teacherinfo
as
select tno,tname,ttelephone
from teacher;

--创建视图：用于查看三二一师生关系信息
create view view_relativeinfo
as
select tname,tno,ttelephone,sname,sno,stelephone,spname,sptelephone,attention
from relative;


--添加信息
--向学生表添加信息
insert into student (sno,sname,major,class,sgender,birthday,stelephone,dorm,dormnum,liveplace) values (sno, sname, major, cls, sgender, birthday, stelephone, dorm, dormnum, liveplace);
--向老师表添加信息
insert into teacher(tno,tname,tgender,ttelephone,tcareer) values (tno, tname, tgender, ttelephone, tcareer);
--向三二一师生关系表添加信息
insert into relative(tname,tno,ttelephone,sname,sno,stelephone,spname,sptelephone,attention) values (tname2, tno2, ttelephone2, sname2, sno2, stelephone2, spname, sptelephone, attention);
--向三二一活动统计表添加信息
insert into calculate(tno,tname,acnumber) values (tno3, tname3, acnumber);

--删除信息
--根据学号删除学生信息(spnum为输入的学号)
delete from student where sno = 'spnum';
--根据姓名删除学生信息(spname为输入的姓名) 
delete from student where sname = 'spname';
--根据班级删除学生信息(spclass为输入的班级)   
delete from student where class = 'spclass';
--根据工号删除教师信息(tpnum为输入的工号)
delete from teacher where tno = 'tpnum';        
--根据姓名删除教师信息(tpname为输入的姓名)
delete from teacher where tname = 'tpname';
--根据学生学号删除三二一师生关系(删除学生表的学生信息)(sqnum为输入的学号)
delete from relative where sno = 'sqnum';
--根据学生姓名删除三二一师生关系(删除学生表的学生信息)(sqname为输入的姓名)
delete from relative where sname = 'sqname';

--修改信息
--根据学号修改学生信息(newtelephone newdorm newdormnum num为新的电话号码，新宿舍楼号，新宿舍房号，学生学号)
update student set stelephone = 'newtelephone' where sno = 'num';  
update student set dorm = 'newdorm' where sno = 'num';
update student set dormnum = 'newdormnum' where sno = 'num';
--根据姓名修改学生信息(newtelephone1 newdorm1 newdormnum1 name为新的电话号码，新宿舍楼号，新宿舍房号，学生姓名)      
update student set stelephone = 'newtelephone1' where sname = 'name';
update student set dorm = 'newdorm1' where sname = 'name';
update student set dormnum = 'newdormnum1' where sname = 'name';
--根据工号修改教师信息(newtelephone2 newtcareer num2 为新的电话号码 新职务 教师工号)
update teacher set ttelephone = 'newtelephone2' where tno = 'num2';
update teacher set tcareer = 'newtcareer' where tno = 'num2';
--根据姓名修改教师信息(newtelephone3 newtcareer3 name2 为新的电话号码 新职务 教师姓名)    
update teacher set ttelephone = 'newtelephone3' where tname = 'name2';
update teacher set tcareer = 'newtcareer3' where tname = 'name2';
--根据教师工号修改三二一活动次数统计信息(newacnumber num3为新的活动次数 教师工号)
update calculate set acnumber = 'newacnumber' where tno = 'num3';    
--根据教师姓名修改三二一活动次数统计信息(newacnumber2 name3为新的活动次数 教师姓名)
update calculate set acnumber = 'newacnumber2' where tname = 'name3';
--根据学生学号修改三二一师生关系信息(newsptelephone num5 为新家长电话号码 学生学号)
update relative set sptelephone = 'newsptelephone' where sno = 'num5'; 
--根据学生姓名修改三二一师生关系信息(newsptelephone2 name4为新家长电话号码 学生姓名)       
update relative set sptelephone = 'newsptelephone2' where sname = 'name4';

--查询信息
--根据学号查询学生信息
select * from student where sno = 'num';        
--根据姓名查询学生信息
select * from student where sname = 'name';       
--查询所有学生信息
select * from student;
--根据工号查询教师信息
select * from teacher where tno = 'num2';    
--根据姓名查询教师信息
select * from teacher where tname = 'name2';     
--查询所有教师信息
select * from teacher;
--根据教师工号查询三二一师生关系信息
select * from relative where tno = 'num3';      
--根据教师姓名查询三二一师生关系信息
select * from relative where tname = 'name3';       
--根据学生学号查询三二一师生关系信息
select * from relative where sno = 'num4';
--根据学生姓名查询三二一师生关系信息
select * from relative where sname = 'name4';       
--查询所有三二一师生关系信息
select * from relative;
--根据教师工号查询活动次数信息
select * from calculate where tno = 'num5';    
--根据教师姓名查询活动次数信息
select * from calculate where tname = 'name5';
--查询所有教师三二一活动次数信息
select * from calculate;                                  