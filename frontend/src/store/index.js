import { createStore } from 'vuex';

export default createStore({
  state: {
    isAuthenticated: false,
    user: null,
  },
  mutations: {
    setUser(state, user) {
      state.isAuthenticated = true;
      state.user = user;
    },
    clearUser(state) {
      state.isAuthenticated = false;
      state.user = null;
    },
  },
  actions: {
    login({ commit }, user) {
      commit('setUser', user);
    },
    logout({ commit }) {
      commit('clearUser');
    },
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    user: (state) => state.user,
  },
});
