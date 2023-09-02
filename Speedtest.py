import speedtest
import logging
import time

LOG_FILE = 'speedtest.log'

def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def setup_logging():
    logging.basicConfig(

        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M",
    )

def main():
    setup_logging()
    while(True):
        d, u, p = test()
        logging.info("%5.1f %5.1f %5.1f", p, d/(1024*1024), u/(1024*1024))
        time.sleep(600)
    '''
    with open('file.txt', 'w') as f:
        for i in range(3):
            print('Making test #{}'.format(i+1))
            d, u, p = test()
            f.write('Test #{}\n'.format(i+1))
            f.write('Download: {:.2f} Mb/s\n'.format(d / (1024*1024)))
            f.write('Upload: {:.2f} Mb/s\n'.format(u / (1024*1024)))
            f.write('Ping: {}\n'.format(p))
    '''

if __name__ == '__main__':
    main()
