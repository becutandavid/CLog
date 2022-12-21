from Drain import LogParser
'424183,424185,2018-06-26,03:36:49.273579,None,INFO,[sample_workload.sh]:,Details:,1,foreground,FAILURE,NO_FAILURE,not_applicable,not_applicable,FAILURE_VOLUME_ATTACHED,NO_FAILURE,2018-06-26 03:36:49.273579,10,2,2babe530,Details:,[],0,91'

log_format = '<real_index>,<line_id>,<timestamp>,<hour>,<pid>,<level>,<service>,<Content>,<test_id>,<parent_service>,<round_1>,<round_2>,<api_round_1>,<api_round_2>,<assertions_round_1>,<assertions_round_2>,<time_hour>,<clusters>,<round>,<EventId>,<EventTemplate>,<ParameterList>,<anom_label>,<encoded_labels>'
log_file = 'data/OpenStack_data_original.csv'
input_dir = 'data/input_drain/'
output_dir = './'

with open(log_file) as f:
    parser = LogParser(log_format, f, indir=input_dir, outdir=output_dir, 
    depth=5, st=0.45)
    templates, df_templates = parser.parse(log_file)
