const sinon = require("sinon");
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payement');

describe('sendPaymentRequestToApi', function() {
    it('validate the usage of the Utils function', function() {
        const test = sinon.spy(Utils, 'calculateNumber');

        sendPaymentRequestToApi(100, 20);

        test.restore();
        sinon.assert.calledOnce(test);
        sinon.assert.calledWith(test, 'SUM', 100, 20);
    });
});
