from yoomoney import Authorize

Authorize(
    client_id="A7DED1A593309E04FF36D3BF817E21CEDF1E8C330F6BC715574E06D81D9D748A",
    redirect_uri="https://t.me/my_first_VPN_bot",
    scope=["account-info",
           "operation-history",
           "operation-details",
           "incoming-transfers",
           "payment-p2p",
           "payment-shop",
           ]
)
