namespace rime {
    class ConfigItem {
        public:
        enum ValueType {kNull, kScalar, kList, kMap};
        ConfigItem() = default;
        virtual ~ConfigItem();

        ValueType type() const { return type_;}

        protected:
            ConfigItem(ValueType type): type_(type) {} 
            ValueType type_ = kNull;
    }

    class ConfigValue: public ConfigItem {
        public:
        ConfigValue(): ConfigItem(kScalar) {}
        ConfigValue(bool value);
        ConfigValue(int value);
        ConfigValue(double value);
        ConfigValue(const char* value);
        ConfigValue(const string& value);

        bool GetBool(bool* value) const;
        
        bool GetInt(int* value) const;
        bool GetDouble(double* value) const;
        bool GetString(string* value) const;
        bool setBool(bool value);
        bool setDouble(double value);
        bool SetString(const char* value);
        bool SetString(const string* value);

        const string &str() const {return value_;}
        protected:
        string value_;

    }

    class ConfigList: public ConfigItem {
        public:
        using Sequence = vertor<an<ConfigItem>>
        using Iterator = Sequence::iterator;
        
        ConfigList(): ConfigItem(kList) {}

        an<ConfigItem> GetAt(size_t i) const;
        an<ConfigValue> GetValueAt(size_t i) const;

        bool SetAt(size_t i, an<ConfigItem> element);
        

        protected:
            Sequence seq_;
    }
};
