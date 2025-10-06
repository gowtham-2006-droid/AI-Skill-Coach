# 🧠 NeuroSkill Coach 2030

> An adaptive AI mentor that evolves with the user, blending neuroscience-inspired motivation with personalized AI skill training.

![NeuroSkill Coach 2030](https://img.shields.io/badge/Version-1.0.0-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.37.1-red) ![Gemini AI](https://img.shields.io/badge/Gemini-2.0--Flash-green)

## 🌌 Concept

NeuroSkill Coach 2030 is a **futuristic web application** that acts as your personal AI mentor. It combines cutting-edge AI technology with neuroscience principles to create an adaptive learning experience that feels alive and responsive to your emotional state and learning patterns.

### Key Features

- 🧭 **Neural Dashboard** - Visualize your learning "mind tree" with animated progress rings
- 🤖 **AI Mentor Chat** - Conversational AI with adaptive tone based on your mood
- 🧩 **Dynamic Skill Simulations** - Generate personalized learning challenges
- 🌱 **Growth Tracker** - Monitor your learning journey with engagement metrics
- 💬 **Mood-Adaptive Coaching** - AI adjusts responses based on your current state
- 🌌 **Vision Mode** - Get AI-generated insights about your future potential

## ⚙️ Tech Stack

- **Frontend & Backend**: Streamlit (Python)
- **AI Engine**: Google Gemini API (gemini-2.0-flash)
- **Data Storage**: Local JSON (`data/user_data.json`)
- **UI Design**: Custom gradients, glassmorphism cards, animated progress rings
- **Environment**: Python virtual environment with `.env` configuration

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone or download the project**
   ```bash
   cd "C:\Users\admin\AI Skill Coach"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   .\.venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure API key**
   ```bash
   # Create .env file with your Gemini API key
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

7. **Open your browser**
   Navigate to `http://localhost:8501`

## 🎯 Usage Guide

### Getting Started

1. **First Launch**: The app creates default data with sample skills (Python, Public Speaking)
2. **Add Skills**: Use the sidebar to add or update your learning skills
3. **Set Mood**: Choose your current emotional state (focused, tired, motivated, etc.)
4. **Chat**: Start a conversation with your AI mentor
5. **Simulate**: Generate learning challenges for any topic
6. **Track Growth**: Monitor your progress and engagement over time

### Features Deep Dive

#### 🧭 Neural Dashboard
- View AI-generated daily summaries of your learning momentum
- See animated progress rings for each skill
- Monitor energy levels and skill mastery

#### 🤖 AI Mentor Chat
- Streamed responses for immersive experience
- Adaptive tone based on your mood and preferences
- Context-aware conversations using your learning data

#### 🧩 Dynamic Skill Simulation
- Enter any topic (e.g., "Python loops", "public speaking")
- Choose simulation type: quiz, scenario, or challenge
- Complete challenges to boost your mind tree energy

#### 🌱 Growth Tracker
- View recent engagement activities
- Log focus sessions and learning milestones
- Track energy boosts across all skills

#### 🌌 Vision Mode
- Generate 6-month future projections
- Get AI insights about your potential growth
- Visualize your learning trajectory

## 📁 Project Structure

```
NeuroSkill Coach 2030/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API key)
├── data/
│   └── user_data.json    # User data storage
├── lib/
│   ├── data_store.py     # JSON data management
│   ├── gemini_client.py  # Gemini API wrapper
│   └── styles.py         # Custom CSS and UI components
└── assets/               # Static assets (future use)
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Customization

- **Model Selection**: Change the Gemini model in `lib/gemini_client.py`
- **UI Themes**: Modify colors and styles in `lib/styles.py`
- **Default Data**: Update initial skills in `lib/data_store.py`

## 🎨 UI Features

- **Glassmorphism Design**: Modern glass-like cards with backdrop blur
- **Gradient Backgrounds**: Futuristic color schemes
- **Animated Progress Rings**: SVG-based skill visualization
- **Responsive Layout**: Works on desktop and mobile
- **Dark Theme**: Easy on the eyes for extended use

## 📊 Data Management

- **Local Storage**: All data saved to `data/user_data.json`
- **Privacy First**: No external data transmission beyond Gemini API
- **Backup Friendly**: Simple JSON format for easy backup/restore
- **Extensible**: Easy to add new data fields and features

## 🛠️ Development

### Adding New Features

1. **New UI Components**: Add to `lib/styles.py`
2. **Data Models**: Extend `lib/data_store.py`
3. **AI Features**: Enhance `lib/gemini_client.py`
4. **App Logic**: Modify `app.py`

### Testing

```bash
# Test API connection
python -c "from lib.gemini_client import GeminiCoach; print('API working!')"

# Test data operations
python -c "from lib.data_store import UserDataStore; store = UserDataStore('data/test.json'); print('Data store working!')"
```

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure `.env` file exists with `GEMINI_API_KEY=your_key`
   - Verify API key is valid and has Gemini access

2. **Model Not Found**
   - Check available models with the test script
   - Update model name in `lib/gemini_client.py`

3. **Port Already in Use**
   - Streamlit will automatically find an available port
   - Or specify: `streamlit run app.py --server.port 8502`

4. **Virtual Environment Issues**
   - Ensure you're in the correct directory
   - Use full path: `C:\Users\admin\AI Skill Coach\.venv\Scripts\activate`

### Getting Help

- Check the terminal output for detailed error messages
- Verify all dependencies are installed: `pip list`
- Test API connectivity separately

## 🚀 Future Enhancements

- [ ] **Multi-language Support**
- [ ] **Advanced Analytics Dashboard**
- [ ] **Skill Recommendation Engine**
- [ ] **Social Learning Features**
- [ ] **Mobile App Version**
- [ ] **Integration with Learning Platforms**
- [ ] **Advanced Visualization Options**
- [ ] **Export/Import Learning Data**

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- **Google Gemini AI** for the powerful language model
- **Streamlit** for the amazing web framework
- **Neuroscience Research** for inspiration on learning optimization

---

**Built with ❤️ for the future of personalized learning**

*NeuroSkill Coach 2030 - Where AI meets neuroscience to unlock your potential*
