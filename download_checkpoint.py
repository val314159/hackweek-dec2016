import os, sys

def main():
    try:
        arg = sys.argv[1]
    except IndexError:
        print "Need argument, try --ls for list of models"
        exit(1)
    if arg=='--ls':
        print """LIST OF MODELS
vgg16
vgg19
inception_v1
inception_v2
inception_v3
inception_resnet_v2
inception_v4
resnet_v1_50
resnet_v1_101
resnet_v1_152
"""
    elif arg=='vgg16':
        download('vgg_16_2016_08_28.tar.gz',
                 'vgg_16.ckpt')
    elif arg=='vgg19':
        download('vgg_19_2016_08_28.tar.gz',
                 'vgg_19.ckpt')
    elif arg=='inception_v1':
        download('inception_v2_2016_08_28.tar.gz',
                 'inception_v1.ckpt')
    elif arg=='inception_v2':
        download('inception_v2_2016_08_28.tar.gz',
                 'inception_v2.ckpt')
    elif arg=='inception_v3':
        download('inception_v3_2016_08_28.tar.gz',
                 'inception_v3.ckpt')
    elif arg=='inception_resnet_v2':
        download('inception_resnet_v2_2016_08_30.tar.gz',
                 'inception_resnet_v2_2016_08_30.ckpt')
    elif arg=='inception_v4':
        download('inception_v4_2016_09_09.tar.gz',
                 'inception_v4.ckpt')
    elif arg=='resnet_v1_50':
        download(
            'resnet_v1_50_2016_08_28.tar.gz',
            'resnet_v1_50.ckpt')
    elif arg=='resnet_v1_101':
        download(
            'resnet_v1_101_2016_08_28.tar.gz',
            'resnet_v1_101.ckpt')
    elif arg=='resnet_v1_152':
        download(
            'resnet_v1_152_2016_08_28.tar.gz',
            'resnet_v1_152.ckpt')
    else:
        print "Model Not Found, try --ls for list of models"
        exit(1)
        
def download(filename, checkpoint_name):
    ret = os.system('''
CHECKPOINT_DIR=/data/checkpoints
mkdir $CHECKPOINT_DIR
wget http://download.tensorflow.org/models/{filename}
tar -xvf {filename}
mv {checkpoint_name} $CHECKPOINT_DIR
rm {filename}
echo COMPLETE
    '''.format(filename=filename, checkpoint_name=checkpoint_name))
    print "RET", ret

if __name__=='__main__': main()
