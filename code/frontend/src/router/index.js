/* eslint-disable camelcase */
import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import upload from '@/components/upload'
import file_list from '@/components/file_list'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/upload',
      name: 'upload',
      component: upload
    },
    {
      path: '',
      name: 'file_list',
      component: file_list
    }
  ]
})
