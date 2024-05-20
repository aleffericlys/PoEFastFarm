import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/calculator',
    name: 'calculator',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/CalculatorView.vue')
  },
  {
	path: '/about/oils',
	name: 'oils',
	component: () => import(/* webpackChunkName: "oils" */ '../views/Oils.vue')
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
