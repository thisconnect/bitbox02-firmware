// Copyright 2019 Shift Cryptosecurity AG
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "commander_eth.h"

#include <stdint.h>
#include <stdio.h>

#include <apps/eth/eth_sign.h>

static commander_error_t _api_sign(const ETHSignRequest* request, ETHSignResponse* response)
{
    app_eth_sign_error_t result = app_eth_sign(request, response);
    if (result == APP_ETH_SIGN_ERR_USER_ABORT) {
        return COMMANDER_ERR_USER_ABORT;
    }
    if (result != APP_ETH_SIGN_OK) {
        return COMMANDER_ERR_GENERIC;
    }
    return COMMANDER_OK;
}

commander_error_t commander_eth(const ETHRequest* request, ETHResponse* response)
{
    switch (request->which_request) {
    case ETHRequest_sign_tag:
        response->which_response = ETHResponse_sign_tag;
        return _api_sign(&(request->request.sign), &response->response.sign);
    default:
        return COMMANDER_ERR_GENERIC;
    }
    return COMMANDER_OK;
}
