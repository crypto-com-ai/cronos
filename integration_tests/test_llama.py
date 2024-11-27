import eth_abi

from .utils import ADDRS, CONTRACTS, deploy_contract, send_transaction


def test_call(cronos):
    w3 = cronos.w3
    addr = ADDRS["validator"]
    contract = deploy_contract(w3, CONTRACTS["TestLLama"])
    prompt = "say hello"
    seed = 2
    steps = 256
    data = {"from": addr, "gasPrice": w3.eth.gas_price, "gas": 600000}
    tx = contract.functions.inference(prompt, seed, steps).build_transaction(data)
    receipt = send_transaction(w3, tx)
    assert receipt.status == 1
    assert len(receipt.logs) == 1

    # decode the event
    rspprompt, rsp = eth_abi.decode(("string", "string"), receipt.logs[0].data)
    assert rspprompt == prompt
    assert rsp == (
        "say helloeymy and Mabel. She was sock. Suddenled. piram the child, "
        "she was called out of adventure came over there. The little Because. Jim "
        "croak filter back down the child stepped in the small legs she was aunt to "
        "sign and she and around her eyes! icy her clung and saw the second.\nThe "
        "corner of her name - had gone. She flever.\nTen way and she had become a "
        "lotion'dled again. Symbol started feeling filled the two, even heard. recogn "
        "reached for a bro welcome child with gates that she asked her head to the "
        "headdled, the old mistake.\nOne knee forward.\nLittle feet called in return "
        "again. LSpace. She was a piece of his name: her furryed: a wooden become the "
        "Mouse to shower warmly, her heart.\nInodedded towards the mouse mock was a "
        "disagreak.\nHer home.\nThe rossy hazoint a second, she was.\nNow, mesint "
        "telling Coraed “His and Joe had come from top. The gifted heart and she "
        "noticed the stroked heart, so many little child.\nMatt."
    )
