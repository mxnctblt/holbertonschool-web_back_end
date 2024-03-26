const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
    it('Validates the usage of the Utils function', function() {
        const test = sinon.spy(Utils, 'calculateNumber');

        sendPaymentRequestToApi(100, 20);

        test.restore();
        sinon.assert.calledOnce(test);
        sinon.assert.calledWith(test, 'SUM', 100, 20);
    });
    it('Verify that the stub is being called', function() {
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
        const log = sinon.spy(console, 'log');

        sendPaymentRequestToApi(100, 20);

        stub.restore();
        log.restore();
        sinon.assert.calledOnce(stub);
        sinon.assert.calledWith(stub, 'SUM', 100, 20);
        sinon.assert.calledWith(log, 'The total is: 10');
    });
});
