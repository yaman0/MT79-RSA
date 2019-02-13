import argparse

from src import RSA, StringTool


def crypt(args):
    message = StringTool.stringToInt(args.message)
    message = RSA.chiffrement(message, args.n, args.d)
    print StringTool.intToString(message)


def decrypt(args):
    message = StringTool.stringToInt(args.message)
    message = RSA.dechiffrement(message, args.n, args.d)
    print StringTool.intToString(message)


def decode(args):
    message = StringTool.stringToInt(args.message)
    d = RSA.findPrivateKey(args.n, args.c)
    message = RSA.dechiffrement(message, args.n, d)
    print StringTool.intToString(message)

def stringtonumber(args):
    print StringTool.stringToInt(args.string)

def numbertostring(args):
    print StringTool.stringToInt(args.number)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest='cmd')
    subparser.required = True
    crypt_parse = subparser.add_parser('crypt', help='Crypt message')
    crypt_parse.add_argument("message", help="message to crypt",
                             type=str)
    crypt_parse.add_argument("n", help="n from private key",
                             type=int)
    crypt_parse.add_argument("d", help="d from private key",
                             type=int)
    crypt_parse.set_defaults(func=crypt)
    crypt_parse = subparser.add_parser('crypt', help='Crypt message')

    decode_parse = subparser.add_parser('decode', help='Crypt message')
    decode_parse.add_argument("message", help="message to decode",
                              type=str)
    decode_parse.add_argument("n", help="n from public key",
                              type=int)
    decode_parse.add_argument("c", help="c from public key",
                              type=int)
    decode_parse.set_defaults(func=decode)

    decrypt_parse = subparser.add_parser('decrypt', help='Crypt message')
    decrypt_parse.add_argument("message", help="message to decrypt",
                               type=str)
    decrypt_parse.add_argument("n", help="n from public key",
                               type=int)
    decrypt_parse.add_argument("d", help="d from public key",
                               type=int)
    decrypt_parse.set_defaults(func=decrypt)

    stn_parse = subparser.add_parser('stn', help='String to number')
    stn_parse.add_argument("string", help="String to number",
                               type=str)
    stn_parse.set_defaults(func=stringtonumber)

    nts_parse = subparser.add_parser('nts', help='Number to string')
    nts_parse.add_argument("number", help="Number to string",
                           type=int)
    nts_parse.set_defaults(func=numbertostring)

    args = parser.parse_args()
    args.func(args)
