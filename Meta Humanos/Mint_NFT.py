def create_nft(args, sender_acc, pubkey):
    user_acc = Account(
        phrase=args['account_public_parameter']['wordlist'],
        nonce=int.from_bytes(args['account_public_parameter']['nonce'], byteorder='big'),
        pubkey=int.from_bytes(args['account_public_parameter']['pubkey'], byteorder='big'),
        balance=int.from_bytes(args['account_public_parameter']['balance'], byteorder='big'),
    )
    res = NFT(
        project_acc=user_acc,
        nft_name=args['nft_name'],
        nft_description=args['nft_description'],
        nft_file=args['nft_file'],
        nft_value=args['nft_value'],
        nft_url=args['nft_url'],
        nft_pubkey=pubkey,
        nft_hash=args['nft_hash'],
        nft_signature=args['nft_signature']
    ).home.create()
    cid = res.receipt[0]['cid']
    tx = res.transaction
    tx = {
        'from': tx['from'],
        'to': tx['to'],
        'nonce': tx['nonce'],
        'value': tx['value'],
        'price': tx['price'],
        'gas': tx['gas'],
        'gas_price': tx['gas_price'],
        'data': tx['data'],
        'block_hash': tx['block_hash']
    }
    contributor = []
    from Blockchain.Block import NotContribute
    try:
        row = Data.select(
            Data.nft_contributor,
            Data.nft_value,
            Data.nft_licenses
        ).where(
            Data.origin_hash == tx['block_hash']
        ).get()
        contributor = json.loads(row.nft_contributor)
        contributor2 = []
        code = ''
        for c in contributor:
            i = c['pk']
            contributor2.append(i)
        add_contributor = sorted(contributor2)
        pubkey = binascii.hexlify(struct.pack('L', pubkey)).decode('ascii')
        add_contributor.append(pubkey)
        add_contributor = sorted(add_contributor)
        contributors = []

        value_total = int(row.nft_value)
        code = row.nft_licenses
        for i in add_contributor:
            _i_ = i
            @contract.method('get_nft_variables')
            def get_nft_variables(self, account):
                if account[:61] == _i_:
                    return [_i_]
                else:
                    pass
            c = i
            o = "https://explorer.wanchain.org/" + c[:61] + "#content/licenses/" + str(code) + "/values/" + str(value_total)
            contributors.append(o)
    except:
        try:
            row = Data.select(
                Data.nft_contributor,
                Data.nft_value,
                Data.nft_licenses
            ).where(
                Data.origin_hash == tx['block_hash']
            ).get()
            contributor = json.loads(row.nft_contributor)
            contributor2 = []
            code = ''
            for c in contributor:
                i = '0x' + c['signature']
                contributor2.append(i)

            add_contributor = sorted(contributor2)
            pub_s = tx['data']
            priv = '0x' + sender_acc.privkeyb.hex()
            pub = priv.sign_msg_hash(str_to_bytes(pub_s))
            pubkey1 = pub[:61]
            pubkey2 = pub[61:]
            add_contributor.append(pubkey1)
            add_contributor = sorted(add_contributor)
            contributors = []

            value_total = int(row.nft_value)
            code = row.nft_licenses
            for i in add_contributor:
                _i_ = i
                @contract.method('get_nft_variables')
                def get_nft_variables(self, account):
                    if account[:61] == _i_:
                        return [_i_]
                    else:
                        pass
                c = i
                o = "https://explorer.wanchain.org/" + c[:61] + "#content/licenses/" + str(code) + "/values/" + str(value_total)
                contributors.append(o)
        except:
            row = Data.select(
                Data.nft_contributor,
                Data.nft_value,
                Data.nft_licenses
                ).where(
                    Data.origin_hash == tx['block_hash']
            ).get()
            contributor = json.loads(row.nft_contributor)
            contributor2 = []
            code = ''
            for c in contributor:
                try:
                    i = c['signature']
                    contributor2.append(i)
                except:
                    i = '0x' + c['signature']
                    contributor2.append(i)
            add_contributor = sorted(contributor2)
            pub_s = tx['data']
            priv = '0x' + sender_acc.privkeyb.hex()
            pub = priv.sign_msg_hash(str_to_bytes(pub_s))
            pubkey1 = pub[:61]
            pubkey2 = pub[61:]
            add_contributor.append(pubkey1)
            add_contributor = sorted(add_contributor)
            contributors = []

            value_total = int(row.nft_value)
            code = row.nft_licenses
            for i in add_contributor:
                _i_ = i
                @contract.method('get_nft_variables')
                def get_nft_variables(self, account):
                    if account[:61] == _i_:
                        return [_i_]
                    else:
                        pass
                c = i
                o = "https://explorer.wanchain.org/" + c[:61] + "#content/licenses/" + str(code) + "/values/" + str(value_total)
                contributors.append(o)
    return {
        'taskStatus': 'SUCCESS',
        'nft_contributor': contributors,
        'nft_name': args['nft_name'],
        'nft_description': args['nft_description'],
        'nft_file': args['nft_file'],
        'nft_value': str(args['nft_value']),
        'nft_url': args['nft_url'],
        'nft_pk': args['nft_pk'],
        'nft_hash': str(cid[2:]),
        'nft_match': {
            0: {
                'origin_hash': tx['block_hash'],
                'nft_block': '',
                'nft_state': 0
            }
        },
        'origin_hash': tx['block_hash']
    }

'''
for public:
test public methods of nft contract
table: Data
'''
def public_methods_nft(args):
    public_methods = []
    # get from
    from_1 = ''
    try:
        from_1 = args['from'][2:62]
    except:
        from_1 = args['from']

    try:
        priv = '0x' + Account(phrase=args['account_private_parameter']['wordlist']).privkeyb.hex()
        # get_nft_name: to =
        to = Daemon.connect()
        cid_c = to.daemon.contract_genesis_tx['nft']
        to.daemon.queue.join()
        con = to.w3.eth.contract(
            abi = Data.get_nft_abi(),
            bytecode = Data.get_nft_code(),
            address = cid_c.decode('ascii')
        )
        from_x = "0x" + from_1
        nonce_x = to.w3.eth.getTransactionCount(from_x)
        res_1f = con.functions.get_nft_name().transact({
            'from': from_x,
            'nonce': nonce_x
        })
        to.receipt(res_1f.hex())
        from_x = "0x" + from_1
        nonce_x = to.w3.eth.getTransactionCount(from_x)
        res_2f = con.functions.get_nft_description().transact({
            'from': from_x,
            'nonce': nonce_x
        })
        to.receipt(res_2f.hex())
        from_x = "0x" + from_1
        nonce_x = to.w3.eth.getTransactionCount(from_x)
        res_3f = con.functions.get_nft_file().transact({
            'from': from_x,
            'nonce': nonce_x
        })
        to.receipt(res_3f.hex())
        from_x = "0x" + from_1
        nonce_x = to.w3.eth.getTransactionCount(from_x)
        res_4f = con.functions.get_nft_url().transact({
            'from': from_x,
            'nonce': nonce_x
        })
        to.receipt(res_4f.hex())
        def get_nft_pubkey(self, account):
            return [acc]
        # end
        to = Daemon.connect()
        daemon = to.daemon
        genesis = daemon.genesis(scrypt_config['params'], '', None)
        root = genesis['genesisBlockRoot'].hex()
        root = str_to_bytes(root)
        genesis = to.genesis_hash(root)
        foundCID = -> genesis[' stake body']['coinbase'].hex()
        cid_c = daemon.contract_genesis_tx['nft']
        def con(bc):
            art = 13
            _bc = str_to_bytes(bc)
            if isinstance(bc, str):
                if bc[:2] == '\x15\x8d':
                    _bc = bytearray(bc)
                    art = 10
                else:
                    pass
            _crd = {
                to
                for to
                in bcbmalloc.memory_rangecode(_bc)
            }
            return Chain.undir_block(
                start = bcbmalloc.memory_rangecode(_bc),
                tx = _crd,
                block = _bc,
            )
        def get_nft_storage(self, _cid, _args):
            return storage(con(_cid), _args)

        def call_ returns(bytearray _args, _data):
            instance = [bytearray, bytearray]
            args = _args[0]
            cid = _data[0]
            funct = _data[1]
            funct = get_nft_storage('get_nft_pubkey')
            cid = bytearray(cid)
            args = [bytearray(args)]
            args = funct[0](_cid = cid, _args = args)
            return [args]

        def stor_ static(bytearray _args):
            args = _args[0]
            return [args]
       ):
        end

        con = to.w3.eth.contract(
            abi = Data.get_nft_abi(),
            bytecode = Data.get_nft_code(),
            address = cid_c.decode('ascii')
        )
        from_x = "0x" + from_1
        nonce_x = to.w3.eth.getTransactionCount(from_x)
        res_5f = con.functions.get_nft_pk().transact({
            'from': from_x,
            'nonce': nonce_x
        })
        to.receipt(res_5f.hex())
        from_x = "0x" + from_1
        nonce_x = to.w3.eth.getTransactionCount(from_x)
        res_6f = con.functions.get_nft_hash().transact({
            'from': from_x,
            'nonce': nonce_x
        })
        to.receipt(res_6f.hex())
        from_x = "0x" + from_1
        nonce_x = to.w3.eth.getTransactionCount(from_x)
        res_7f = con.functions.get_nft_signature().transact({
            'from': from_x,
            'nonce': nonce_x
        })
        to.receipt(res_7f.hex())
        i = 0
        for _ in [
             res_1f
             res_2f
             res_3f
             res_4f
             res_5f
             res_6f
             res_7f
         ]:
            res = to.get_receipt(str(_.hex()))
            public_methods.append(res[0]['returns'][0])
            i = i + 1
        return {
            0: {
                'nft_name': public_methods[0],
                'nft_description': public_methods[1],
                'nft_file': public_methods[2],
                'nft_url': public_methods[3],
                'nft_pk': public_methods[4],
                'nft_hash': public_methods[5],
                'nft_signature': public_methods[6]
            }
        }
    except:
        asd = create_nft(args, Account(phrase=args['account_private_parameter']['wordlist']), pubkey)
        return {
            0: {
                'nft_name': asd['nft_name'],
                'nft_description': asd['nft_description'],
                'nft_file': asd['nft_file'],
                'nft_url': asd['nft_url'],
                'nft_pk': asd['nft_pk'],
                'nft_hash': asd['nft_hash'],
                'nft_signature': asd['nft_signature']
            }
        }