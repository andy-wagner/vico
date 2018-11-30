import os

from exp.experimenter import *
from utils.argparse_utils import manage_required_args, str_to_bool
from utils.constants import Constants, ExpConstants
from .models.resnet import ResnetConstants
from .models.resnet_normalized import ResnetNormalizedConstants
from .dataset import ImagenetDatasetConstants
from . import train
from . import entity_entity_reps
#from . import eval as evaluation


def exp_train():
    exp_name = 'multilabel_resnet_50_normalized_adam'
    out_base_dir = os.path.join(
        os.getcwd(),
        'symlinks/exp/imagenet')
    exp_const = ExpConstants(exp_name,out_base_dir)
    exp_const.model_dir = os.path.join(exp_const.exp_dir,'models')
    exp_const.log_dir = os.path.join(exp_const.exp_dir,'log')
    exp_const.vis_dir = os.path.join(exp_const.exp_dir,'vis')
    exp_const.log_step = 10
    exp_const.model_save_step = 10000
    exp_const.vis_step = 5000
    # exp_const.val_step = 1000
    # exp_const.num_val_samples = 1000
    exp_const.batch_size = 32
    exp_const.num_epochs = 20
    exp_const.lr = 0.1
    exp_const.momentum = 0.9
    exp_const.num_workers = 5
    exp_const.optimizer = 'Adam'

    data_const = ImagenetDatasetConstants()

    model_const = Constants()
    model_const.model_num = None
    model_const.net = ResnetNormalizedConstants()
    model_const.net.num_layers = 50
    model_const.net.num_classes = 21841
    model_const.net_path = os.path.join(
        exp_const.model_dir,
        f'net_{model_const.model_num}')

    train.main(exp_const,data_const,model_const)


def exp_compute_entity_entity_reps():
    exp_name = 'multilabel_resnet_18_normalized_adam_entity_entity_reps'
    out_base_dir = os.path.join(
        os.getcwd(),
        'symlinks/exp/imagenet')
    exp_const = ExpConstants(exp_name,out_base_dir)
    exp_const.batch_size = 32
    exp_const.num_workers = 5

    data_const = ImagenetDatasetConstants()

    model_const = Constants()
    model_const.model_num = 930000
    model_const.net = ResnetNormalizedConstants()
    model_const.net.num_layers = 18
    model_const.net.num_classes = 21841
    model_const.net_path = os.path.join(
        os.getcwd(),
        'symlinks/exp/imagenet/multilabel_resnet_18_normalized_adam/' + \
        f'models/net_{model_const.model_num}')

    entity_entity_reps.main(exp_const,data_const,model_const)

# def exp_eval():
#     exp_name = 'EXP_NAME'
#     out_base_dir = os.path.join(
#         os.getcwd(),
#         'symlinks/exp/imagenet')
#     exp_const = ExpConstants(exp_name,out_base_dir)
#     exp_const.model_dir = os.path.join(exp_const.exp_dir,'models')
#     exp_const.log_dir = os.path.join(exp_const.exp_dir,'log')
#     exp_const.vis_dir = os.path.join(exp_const.exp_dir,'vis')
#     exp_const.batch_size = 32
#     exp_const.num_workers = 5

#     data_const = ImagenetDatasetConstants()
#     data_const.subset = 'eval'

#     model_const = Constants()
#     model_const.model_num = None
#     model_const.net = ResnetConstants()
#     model_const.net_path = os.path.join(
#         exp_const.model_dir,
#         f'net_{model_const.model_num}')

#     evaluation.main(exp_const,data_const,model_const)


if __name__=='__main__':
    list_exps(globals())
