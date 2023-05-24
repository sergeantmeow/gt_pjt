<template>
  <div>
    <h2 class="title-mg-ct">Login</h2>
    <div class="container login-color">
      <div class="row justify-content-center">
        <div class="col-md-4">
          <form @submit.prevent="login" class="mt-4">
            <div class="form-group">
            <label for="username">username : </label>
            <input type="text" id="username" v-model="username" class="form-control"><br>
            </div>
            <div class="form-group">
            <label for="password"> password : </label>
            <input type="password" id="password" v-model="password" class="form-control"><br>
            </div>
            <input type="submit" value="로그인" class="btn btn-login fw-bold">
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      this.username = ''
      this.password = ''
      this.$store.dispatch('login', payload)
    }
  },
}
</script>

<style>
.btn-login {
  background-color: #261639;
  color: #bfbfbf;
}

.btn-login:hover {
  background-color: #7c6891;
}

.login-color{
  color : #bfbfbf;
}
</style>