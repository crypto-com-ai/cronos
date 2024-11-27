import eth_abi

from .utils import ADDRS, CONTRACTS, deploy_contract, send_transaction


def test_call(cronos):
    w3 = cronos.w3
    addr = ADDRS["validator"]
    contract = deploy_contract(w3, CONTRACTS["TestLLama"])
    prompt = "say hello"
    seed = 2
    steps = 128
    data = {"from": addr, "gasPrice": w3.eth.gas_price, "gas": 600000}
    tx = contract.functions.inference(prompt, seed, steps).build_transaction(data)
    receipt = send_transaction(w3, tx)
    assert receipt.status == 1
    assert len(receipt.logs) == 1

    # decode the event
    rspprompt, rsp = eth_abi.decode(("string", "string"), receipt.logs[0].data)
    assert rspprompt == prompt
    assert rsp == (
        "say hello Joe and the Zoe, who was ate their favour.\nTweed woke. He was the "
        'next. 3. He was one flately before him. Tom and his best friend.\nBeeped - "I '
        "would lent and the beginning todden. He was 8 with a run.\nEvery day that day "
        'and a story time.\nThe next. He said, "Every day.\nThe go handed out marched, '
        "he loved and he was a ladder. Everyone would prepare. He looked around him "
        "glown towards the other-th him.\nThe"
    )
