import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    'domain',
    help = '스캔할 domain을 입력합니다.'
    )
parser.add_argument(
    '-o','--output',
    help = '결과를 지정한 파일에 저장합니다.',
    dest = 'output_file'
    )
parser.add_argument(
    '-m','--mail',
    help = '결과를 지정한 주소에 보냅니다.',
    dest = 'mail_address'
    )
parser.add_argument(
    '--censys_api_id',
    help = 'Censys_api_id를 지정합니다.',
    dest = 'censys_api_id'
    )
parser.add_argument(
    '--censys_api_secret',
    help = 'Censys_api_secret를 지정합니다.',
    dest = 'censys_api_secret'
    )
