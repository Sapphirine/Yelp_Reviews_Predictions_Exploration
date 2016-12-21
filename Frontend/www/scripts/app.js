angular.module('app', ['ngRoute', 'ngMap', 'ngAnimate'])
    .config(['$routeProvider', function ($route) {
        $route
            .when('/', {
                templateUrl: 'views/map.html',
                controller: 'MapCtrl'
            })
            .when('/:id', {
                templateUrl: 'views/detail.html',
                controller: 'DetailCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
    }]);
