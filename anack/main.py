# -*- coding:utf-8 -*- 

import App.IndustryEstimation
from SQL.sql import pymysql_connect
from SQL.update import get_interest_list
import App.IndustryEstimation_detail

industry_check = []
dbconn=pymysql_connect()
filename = './SQL/感兴趣的个股列表.txt'
stock_code_num = ['600000' ,'600004' ,'600005' ,'600006' ,'600007' ,'600008' ,'600009' ,'600010' ,'600011' ,'600012' ,'600015' ,'600016' ,'600017' ,'600018' ,'600019' ,'600020' ,'600021' ,'600022' ,'600026' ,'600027' ,'600028' ,'600029' ,'600030' ,'600031' ,'600033' ,'600035' ,'600036' ,'600037' ,'600038' ,'600039' ,'600048' ,'600050' ,'600051' ,'600052' ,'600053' ,'600054' ,'600055' ,'600056' ,'600058' ,'600059' ,'600060' ,'600061' ,'600062' ,'600063' ,'600064' ,'600066' ,'600067' ,'600068' ,'600069' ,'600070' ,'600071' ,'600072' ,'600073' ,'600074' ,'600075' ,'600076' ,'600077' ,'600078' ,'600079' ,'600080' ,'600081' ,'600082' ,'600083' ,'600084' ,'600085' ,'600086' ,'600087' ,'600088' ,'600089' ,'600090' ,'600091' ,'600093' ,'600095' ,'600096' ,'600097' ,'600098' ,'600099' ,'600100' ,'600101' ,'600102' ,'600103' ,'600104' ,'600105' ,'600106' ,'600107' ,'600108' ,'600109' ,'600110' ,'600111' ,'600112' ,'600113' ,'600114' ,'600115' ,'600116' ,'600117' ,'600118' ,'600119' ,'600120' ,'600121' ,'600122' ,'600123' ,'600125' ,'600126' ,'600127' ,'600128' ,'600129' ,'600130' ,'600131' ,'600132' ,'600133' ,'600135' ,'600136' ,'600137' ,'600138' ,'600139' ,'600141' ,'600143' ,'600145' ,'600146' ,'600148' ,'600149' ,'600150' ,'600151' ,'600152' ,'600153' ,'600155' ,'600156' ,'600157' ,'600158' ,'600159' ,'600160' ,'600161' ,'600162' ,'600163' ,'600165' ,'600166' ,'600167' ,'600168' ,'600169' ,'600170' ,'600171' ,'600172' ,'600173' ,'600175' ,'600176' ,'600177' ,'600178' ,'600179' ,'600180' ,'600182' ,'600183' ,'600184' ,'600185' ,'600186' ,'600187' ,'600188' ,'600189' ,'600190' ,'600191' ,'600192' ,'600193' ,'600195' ,'600196' ,'600197' ,'600198' ,'600199' ,'600200' ,'600201' ,'600202' ,'600203' ,'600206' ,'600207' ,'600208' ,'600209' ,'600210' ,'600211' ,'600212' ,'600213' ,'600215' ,'600216' ,'600217' ,'600218' ,'600219' ,'600220' ,'600221' ,'600222' ,'600223' ,'600225' ,'600226' ,'600227' ,'600228' ,'600229' ,'600230' ,'600231' ,'600232' ,'600233' ,'600234' ,'600235' ,'600236' ,'600237' ,'600238' ,'600239' ,'600240' ,'600241' ,'600242' ,'600243' ,'600246' ,'600247' ,'600248' ,'600249' ,'600250' ,'600251' ,'600252' ,'600253' ,'600255' ,'600256' ,'600257' ,'600258' ,'600259' ,'600260' ,'600261' ,'600262' ,'600263' ,'600265' ,'600266' ,'600267' ,'600268' ,'600269' ,'600270' ,'600271' ,'600272' ,'600273' ,'600275' ,'600276' ,'600277' ,'600278' ,'600279' ,'600280' ,'600281' ,'600282' ,'600283' ,'600284' ,'600285' ,'600287' ,'600288' ,'600289' ,'600290' ,'600291' ,'600292' ,'600293' ,'600295' ,'600297' ,'600298' ,'600299' ,'600300' ,'600301' ,'600302' ,'600303' ,'600305' ,'600306' ,'600307' ,'600308' ,'600309' ,'600310' ,'600311' ,'600312' ,'600313' ,'600315' ,'600316' ,'600317' ,'600318' ,'600319' ,'600320' ,'600321' ,'600322' ,'600323' ,'600325' ,'600326' ,'600327' ,'600328' ,'600329' ,'600330' ,'600331' ,'600332' ,'600333' ,'600335' ,'600336' ,'600337' ,'600338' ,'600339' ,'600340' ,'600343' ,'600345' ,'600346' ,'600348' ,'600350' ,'600351' ,'600352' ,'600353' ,'600354' ,'600355' ,'600356' ,'600358' ,'600359' ,'600360' ,'600361' ,'600362' ,'600363' ,'600365' ,'600366' ,'600367' ,'600368' ,'600369' ,'600370' ,'600371' ,'600373' ,'600375' ,'600376' ,'600377' ,'600378' ,'600379' ,'600380' ,'600381' ,'600382' ,'600383' ,'600385' ,'600386' ,'600387' ,'600388' ,'600389' ,'600390' ,'600391' ,'600392' ,'600393' ,'600395' ,'600396' ,'600397' ,'600398' ,'600399' ,'600400' ,'600403' ,'600405' ,'600406' ,'600408' ,'600409' ,'600410' ,'600415' ,'600416' ,'600418' ,'600419' ,'600420' ,'600421' ,'600422' ,'600423' ,'600425' ,'600426' ,'600428' ,'600429' ,'600432' ,'600433' ,'600435' ,'600436' ,'600438' ,'600439' ,'600444' ,'600446' ,'600448' ,'600449' ,'600452' ,'600455' ,'600456' ,'600458' ,'600459' ,'600460' ,'600461' ,'600462' ,'600463' ,'600466' ,'600467' ,'600468' ,'600469' ,'600470' ,'600475' ,'600476' ,'600477' ,'600478' ,'600479' ,'600480' ,'600481' ,'600482' ,'600483' ,'600485' ,'600486' ,'600487' ,'600488' ,'600489' ,'600490' ,'600491' ,'600493' ,'600495' ,'600496' ,'600497' ,'600498' ,'600499' ,'600500' ,'600501' ,'600502' ,'600503' ,'600505' ,'600506' ,'600507' ,'600508' ,'600509' ,'600510' ,'600511' ,'600512' ,'600513' ,'600515' ,'600516' ,'600517' ,'600518' ,'600519' ,'600520' ,'600521' ,'600522' ,'600523' ,'600525' ,'600526' ,'600527' ,'600528' ,'600529' ,'600530' ,'600531' ,'600532' ,'600533' ,'600535' ,'600536' ,'600537' ,'600538' ,'600539' ,'600540' ,'600543' ,'600545' ,'600546' ,'600547' ,'600548' ,'600549' ,'600550' ,'600551' ,'600552' ,'600553' ,'600555' ,'600557' ,'600558' ,'600559' ,'600560' ,'600561' ,'600562' ,'600563' ,'600565' ,'600566' ,'600567' ,'600568' ,'600569' ,'600570' ,'600571' ,'600572' ,'600573' ,'600575' ,'600576' ,'600577' ,'600578' ,'600579' ,'600580' ,'600581' ,'600582' ,'600583' ,'600584' ,'600585' ,'600586' ,'600587' ,'600588' ,'600589' ,'600590' ,'600592' ,'600593' ,'600594' ,'600595' ,'600596' ,'600597' ,'600598' ,'600599' ,'600600' ,'600601' ,'600602' ,'600603' ,'600604' ,'600605' ,'600606' ,'600608' ,'600609' ,'600610' ,'600611' ,'600612' ,'600613' ,'600614' ,'600615' ,'600616' ,'600617' ,'600618' ,'600619' ,'600620' ,'600621' ,'600622' ,'600623' ,'600624' ,'600626' ,'600628' ,'600629' ,'600630' ,'600631' ,'600633' ,'600634' ,'600635' ,'600636' ,'600637' ,'600638' ,'600639' ,'600640' ,'600641' ,'600642' ,'600643' ,'600644' ,'600645' ,'600647' ,'600648' ,'600649' ,'600650' ,'600651' ,'600652' ,'600653' ,'600654' ,'600655' ,'600656' ,'600657' ,'600658' ,'600660' ,'600661' ,'600662' ,'600663' ,'600664' ,'600665' ,'600666' ,'600667' ,'600668' ,'600671' ,'600673' ,'600674' ,'600675' ,'600676' ,'600677' ,'600678' ,'600679' ,'600680' ,'600682' ,'600683' ,'600684' ,'600685' ,'600686' ,'600687' ,'600688' ,'600689' ,'600690' ,'600691' ,'600692' ,'600693' ,'600694' ,'600695' ,'600696' ,'600697' ,'600698' ,'600699' ,'600701' ,'600702' ,'600703' ,'600704' ,'600706' ,'600707' ,'600708' ,'600710' ,'600711' ,'600712' ,'600713' ,'600714' ,'600715' ,'600716' ,'600717' ,'600718' ,'600719' ,'600720' ,'600721' ,'600722' ,'600723' ,'600724' ,'600725' ,'600726' ,'600727' ,'600728' ,'600729' ,'600730' ,'600731' ,'600732' ,'600733' ,'600734' ,'600735' ,'600736' ,'600737' ,'600738' ,'600739' ,'600740' ,'600741' ,'600742' ,'600743' ,'600744' ,'600745' ,'600746' ,'600747' ,'600748' ,'600749' ,'600750' ,'600751' ,'600753' ,'600754' ,'600755' ,'600756' ,'600757' ,'600758' ,'600759' ,'600760' ,'600761' ,'600763' ,'600764' ,'600765' ,'600766' ,'600767' ,'600768' ,'600769' ,'600770' ,'600771' ,'600773' ,'600774' ,'600775' ,'600776' ,'600777' ,'600778' ,'600779' ,'600780' ,'600781' ,'600782' ,'600783' ,'600784' ,'600785' ,'600787' ,'600789' ,'600790' ,'600791' ,'600792' ,'600793' ,'600794' ,'600795' ,'600796' ,'600797' ,'600798' ,'600800' ,'600801' ,'600802' ,'600803' ,'600804' ,'600805' ,'600806' ,'600807' ,'600808' ,'600809' ,'600810' ,'600811' ,'600812' ,'600814' ,'600815' ,'600816' ,'600817' ,'600818' ,'600819' ,'600820' ,'600821' ,'600822' ,'600823' ,'600824' ,'600825' ,'600826' ,'600827' ,'600828' ,'600829' ,'600830' ,'600831' ,'600832' ,'600833' ,'600834' ,'600835' ,'600836' ,'600837' ,'600838' ,'600839' ,'600841' ,'600843' ,'600844' ,'600845' ,'600846' ,'600847' ,'600848' ,'600850' ,'600851' ,'600853' ,'600854' ,'600855' ,'600856' ,'600857' ,'600858' ,'600859' ,'600860' ,'600861' ,'600862' ,'600863' ,'600864' ,'600865' ,'600866' ,'600867' ,'600868' ,'600869' ,'600871' ,'600872' ,'600873' ,'600874' ,'600875' ,'600876' ,'600877' ,'600879' ,'600880' ,'600881' ,'600882' ,'600883' ,'600884' ,'600885' ,'600886' ,'600887' ,'600888' ,'600889' ,'600890' ,'600891' ,'600892' ,'600893' ,'600894' ,'600895' ,'600896' ,'600897' ,'600898' ,'600900' ,'600960' ,'600961' ,'600962' ,'600963' ,'600965' ,'600966' ,'600967' ,'600969' ,'600970' ,'600971' ,'600973' ,'600975' ,'600976' ,'600978' ,'600979' ,'600980' ,'600981' ,'600982' ,'600983' ,'600984' ,'600985' ,'600986' ,'600987' ,'600988' ,'600990' ,'600991' ,'600992' ,'600993' ,'600995' ,'600997' ,'600999' ,'601001' ,'601002' ,'601003' ,'601005' ,'601006' ,'601007' ,'601008' ,'601009' ,'601088' ,'601099' ,'601106' ,'601107' ,'601111' ,'601117' ,'601139' ,'601166' ,'601168' ,'601169' ,'601179' ,'601186' ,'601268' ,'601299' ,'601318' ,'601328' ,'601333' ,'601390' ,'601398' ,'601588' ,'601600' ,'601601' ,'601607' ,'601618' ,'601628' ,'601666' ,'601668' ,'601678' ,'601688' ,'601699' ,'601727' ,'601766' ,'601788' ,'601801' ,'601808' ,'601857' ,'601866' ,'601872' ,'601877' ,'601888' ,'601898' ,'601899' ,'601918' ,'601919' ,'601939' ,'601958' ,'601988' ,'601989' ,'601991' ,'601998' ,'601999' ,'000958' ,'601188' ,'601518']




# =============================================================================
# #行业平均数据
# App.IndustryEstimation.CreateTable() #此处开启则清空此前所有内容
# for stock_id in get_interest_list(filename):
#     name = App.IndustryEstimation.GetIndustryName(stock_id) #根据id获取行业名
#     
#     if name in industry_check: #去重检查
#         continue
#     else:
#         industry_check.append(name)
#  
#     App.IndustryEstimation.Estimation(dbconn,name,2017) #入库
# =============================================================================





#行业平均数据明细
# =============================================================================
# App.IndustryEstimation_detail.CreateTable() #此处开启则清空此前所有内容
# App.IndustryEstimation_detail.Estimation() #入库
# =============================================================================
App.IndustryEstimation_detail.industry_stat('通信设备')
App.IndustryEstimation_detail.CreateTable_industry_avg()