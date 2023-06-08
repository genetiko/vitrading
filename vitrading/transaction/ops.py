from nameko.rpc import rpc


class TradingService:
    name = "trading_service"

    @rpc
    def open(self, instrument_id, timestamp, side, stop, send_updates=False) -> str:
        pass

    @rpc
    def close(self, transaction_id):
        pass
