/*global angular */
(function () {
    'use strict';

    // Declare app level module which depends on views, and components
    angular.module('scrumBan')
        .constant('ROLES', [
            {
                displayName: 'Administrator',
                id: 'administrator'
            },
            {
                displayName: 'Scrum master',
                id: 'scrummaster'
            },
            {
                displayName: 'Product owner',
                id: 'productowner'
            },
            {
                displayName: 'Team member',
                id: 'teammember'
            }
        ])
        .constant('USERS', [
            {
                id: 0,
                firstName: 'Rok',
                lastName: 'Rupnik',
                email: 'rok7rupnik@gmail.com',
                roles: ['teammember']
            },
            {
                id: 1,
                firstName: 'Luka',
                lastName: 'Krsnik',
                email: 'krsnik.luka92@gmail.com',
                roles: ['scrummaster']
            },
            {
                id: 2,
                firstName: 'Tone',
                lastName: 'Priimek',
                email: 'tone.primek@gmail.com',
                roles: ['productowner']
            }
        ])
        .constant('API_URL', 'api/');
}());