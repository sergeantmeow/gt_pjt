<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="editArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <div v-if="image">
        <img :src="image" alt="이미지" class="image-preview">
      </div>
      <label for="content">내용 : </label>
      <textarea id="content" cols="50" rows="10" v-model="content"></textarea><br>
      <label for="content">이미지 선택 : </label>
      <input type="file" id="image" ref="image" @change="handleImageChange"><br>
      <input type="submit" id="submit" value="수정">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleEditView',
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
    }
  },
  created(){
    const { title, image, content } = this.$route.query;
    this.title = title;
    this.image = API_URL + image;
    this.content = content;
  },
  methods: {
  editArticle() {

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
      method: 'put',
      url: `${API_URL}/articles/${ this.$route.params.id }/`,
      headers: {
        Authorization: `Token ${this.$store.state.user.token}`,
        'Content-Type': 'multipart/form-data',
      },
      data: formData
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
    },
  }
}
</script>

<style>

</style>
