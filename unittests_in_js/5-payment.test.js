const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
    it('Checks 100 + 20', function() {
        const log = sinon.spy(console, 'log');

        sendPaymentRequestToApi(100, 20);

        log.restore();
        sinon.assert.calledOnce(log);
        sinon.assert.calledWith(log, 'The total is: 120');
    });
    it('Checks 10 + 10', function() {
        const log = sinon.spy(console, 'log');

        sendPaymentRequestToApi(10, 10);

        log.restore();
        sinon.assert.calledOnce(log);
        sinon.assert.calledWith(log, 'The total is: 20');
    });
});
