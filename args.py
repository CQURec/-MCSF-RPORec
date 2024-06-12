import argparse


def get_args():
    parser = argparse.ArgumentParser(description='MCSF-RPORec main.py')
    # dataset params
    parser.add_argument('--dataset', type=str, default="Epinions", help="Epinions, Yelp")
    parser.add_argument('--seed', type=int, default=29)

    parser.add_argument('--hide_dim', type=int, default=32)
    parser.add_argument('--layer', type=str, default="[32]")
    parser.add_argument('--slope', type=float, default=0.4)

    parser.add_argument('--reg', type=float, default=0.05)
    parser.add_argument('--decay', type=float, default=0.98)
    parser.add_argument('--batch', type=int, default=1024)
    parser.add_argument('--lr', type=float, default=0.01)
    parser.add_argument('--minlr', type=float, default=0.0001)
    parser.add_argument('--test_batch', type=int, default=1024)
    parser.add_argument('--epochs', type=int, default=120)
    # early stop params
    parser.add_argument('--patience', type=int, default=120)
    parser.add_argument('--num_ng', type=int, default=1)
    parser.add_argument('--top_k', type=int, default=10)
    parser.add_argument('--fuse', type=str, default="mean", help="mean or weight")

    parser.add_argument('--dgi_graph_act', type=str, default="sigmoid", help="sigmoid or tanh")
    parser.add_argument('--lam', type=str, default='[0.1,0.001]')
    parser.add_argument('--clear', type=int, default=0)
    parser.add_argument('--subNode', type=int, default=10)

    parser.add_argument('--time_step', type=float, default=360)
    parser.add_argument('--startTest', type=int, default=0)
    parser.add_argument('--au_rate', type=int, default=400)
    parser.add_argument('--gamma', type=float, default=0.3)
    parser.add_argument('--gpu', default='cuda:2', type=str, help='indicates which gpu to use')

    # ssl
    parser.add_argument('--ssl_temp', type=float, default=0.25, help='the temperature in softmax')
    parser.add_argument('--ssl_beta', type=float, default=0.01, help='weight of loss with ssl')
    parser.add_argument('--ssl_alpha', type=float, default=0.5, help='weight of loss with ssl')
    return parser.parse_args()
args = get_args()