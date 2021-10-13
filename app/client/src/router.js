import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    routes: [
        {
          path: '/',
          name: 'home',
          component: () => import('./views/Home.vue')
        },
        {
          path: '/concept',
          name: 'concept',
          component: () => import('./views/Concept.vue')
        },
        {
          path: '/contact',
          name: 'contact',
          component: () => import('./views/Contact.vue')
        },
        {
          path: '/form',
          name: 'form',
          component: () => import('./views/Form.vue')
        }
    ]
})