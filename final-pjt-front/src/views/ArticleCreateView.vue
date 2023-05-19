<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <div v-if="image">
        <img :src="image" alt="이미지" class="image-preview">
      </div>
      <label for="content">내용 : </label>
      <textarea id="content" cols="50" rows="10" v-model="content"></textarea><br>
      <label for="content">이미지 선택 : </label>
      <input type="file" id="image" ref="image" @change="handleImageChange"><br>
      <input type="submit" id="submit" value="작성">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      title: '',
      content: '',
      image: '',
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    createArticle() {
      if (!this.title) {
        alert('제목 입력해주세요')
        return
      } else if (!this.content){
        alert('내용 입력해주세요')
        return
      }

      const formData = new FormData();
      formData.append('title', this.title);
      formData.append('content', this.content);
      if (this.image) {
      formData.append('image', this.$refs.image.files[0]);
      }
      
      axios({
        method: 'post',
        url: `${API_URL}/articles/create/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
          'Content-Type' : 'multipart/form-data',
        },
        data: formData,
      })
      .then(() => {
        this.$router.push({name: 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    handleImageChange(event) {
      const file = event.target.files[0]
      const reader = new FileReader()

      reader.onload = (e) => {
        this.image = e.target.result
      }

      reader.readAsDataURL(file)
    }
  }
}
</script>

<style>
.image-preview {
  max-width: 500px;
  max-height: 500px;
}
</style>
