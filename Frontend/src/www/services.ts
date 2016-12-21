/// <reference types="angular" />
interface callback {
    (res: any): void;
}

class HttpService {
    private _urlBase = 'http://localhost:5000';

    static $inject = ['$http'];
    constructor(
        private _http: ng.IHttpService
    ) { }

    init(urlBase: string): void {
        if (urlBase.indexOf('/', urlBase.length - '/'.length) !== -1) {
            this._urlBase = urlBase.substr(0, urlBase.length - 1);
        } else {
            this._urlBase = urlBase;
        }
    }

    get(url: string, onSuccess: callback, onError: callback): void {
        this._http.get(this._urlBase + url)
        .then(onSuccess, onError);
    }

    post(url: string, payload: any, onSuccess: callback, onError: callback): void {
        this._http.post(this._urlBase + url, payload)
        .then(onSuccess, onError);
    }
}

angular.module('app')
    .service('HttpService', HttpService);