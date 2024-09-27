from gmx_python_sdk.scripts.v2.order.create_withdrawal_order import WithdrawOrder
from gmx_python_sdk.scripts.v2.order.liquidity_argument_parser import LiquidityArgumentParser
from gmx_python_sdk.scripts.v2.gmx_utils import ConfigManager

def create_withdraw_order(params):
    config = ConfigManager("arbitrum")
    config.set_config()

    parameters = {
        "chain": params.get("chain"),
        "market_token_symbol": params.get("market_token_symbol"),
        "out_token_symbol": params.get("out_token_symbol"),
        "gm_amount": params.get("gm_amount")
    }

    output = LiquidityArgumentParser(
            config, is_withdrawal=True
        ).process_parameters_dictionary(
            parameters
        )

    WithdrawOrder(
        config=config,
        market_key=output['market_key'],
        out_token=output['out_token_address'],
        gm_amount=output['gm_amount'],
        debug_mode = False
    )
    return "order executed"

# from utils import _set_paths
# _set_paths()
